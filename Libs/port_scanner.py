from socket import *
import threading

lock = threading.Lock()
openNum = 0


def portScanner(host, port):
    global openNum
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        lock.acquire()
        openNum += 1
        print('[+] '+str(port)+'('+str(host)+') open')
        lock.release()
        s.close()
    except:
        pass



def scan(ip):
    global openNum
    hosts = ip.split(';')
    setdefaulttimeout(1)
    for target in hosts:
        openNum = 0
        for n in range(1, 76):
            threads = []
            # print (n-1)*880,n*880
            for p in range((n - 1) * 880, n * 880):
                t = threading.Thread(target=portScanner, args=(target, p))
                threads.append(t)
                t.start()

            for t in threads:
                pass
            t.join()

        print('[*] The scan('+target+') is complete!')
        print('[*] A total of %d open port ' % (openNum))
    print('[*] Done.')





def info():
    print('This module helps you to understand the target.')
    print('Usage: make port_scanner scan [IP/HOSTS]')
    print('Example: make port_scanner scan 192.168.0.101')
    print('Example2: make port_scanner scan 192.168.0.12;192.168.0.13')
