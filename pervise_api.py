# This is Pervise API PyFile
import threading
import time
import socket
import random
import sys
import os
import color
import hashlib
import subprocess
import urllib.request
import requests
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
from qt_material import apply_stylesheet

current = sys.stdout
class redirect:
    content = ""

    def write(self,str):
        self.content += str
    def flush(self):
        self.content = ""
r = redirect()

service_status = False
status = {
    -2 : "[-] Failed to load libraries. Nothing to do.",
    -1 : "[-] Failed to load libraries. Cannot find the folder \"Libs\".",
    0 : "[*] Done."
}

libraries = []

class about(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


def enctry(s,k): # s: string k: password
    k *= 0xFFFF
    encry_str = ""
    for i,j in zip(s,k):
        temp = str(ord(i)+ord(j))+'_'
        encry_str = encry_str + temp
    return encry_str

def dectry(p, k): # d: string k: password
    k *= 0xFFFF
    dec_str = ""
    for i,j in zip(p.split("_")[:-1],k):
        temp = chr(int(i) - ord(j))
        dec_str = dec_str+temp
    return dec_str

def getFilelist(path): # get file list
    return os.listdir(path)

def show_help(command,commands):
    color.printGreen('Help: ')
    for keys in commands:
        color.printGreen(keys)
    if service_status:
        color.printGreen('encrypt true/false')

def show_info(command,commands):
    app = QApplication(sys.argv)
    window = about()
    apply_stylesheet(app, theme='dark_teal.xml')
    color.printGreen('Pervise Beta 3')
    color.printGreen('Powered by tiantian520')
    try:
        sys.exit(app.exec_())
    except:
        pass

def load_libraries():
    try:
        if os.path.exists("./Libs"):
            fileList=getFilelist('./Libs')
            for file in fileList:
                if os.path.isdir("./Libs/"+str(file)):
                    continue
                with open("./Libs/"+str(file),'r',encoding='utf-8') as library:
                    temp = library.read()
                with open("./"+str(file),'w') as library:
                    library.write(temp)
                    libraries.append(os.path.basename(str(file)).split('.')[0])
            for library in libraries:
                __import__(str(library))
                exec("import "+str(library))
                color.printGreen("[*] Library " + str(library) + " loaded.")
            return 0
        else:
            return -1
    except:
        return -2
def make_trojan(command,commands):
    try:
        cmds = str(command).split()
        library = cmds[1]
        __import__(str(library))
        exec("import " + str(library))
        color.printGreen("[*] Library " + str(library) + " loaded.")
    except:
        color.printRed("[-] Failed to load library.")
        color.printGreen('[*] Usage: make module (Tip: list)')
        return -1
    try:
        cmd = cmds[1]+"."+cmds[2]+"("
        for index in range(3,len(cmds)):
            cmd+="\""+cmds[index].replace("\\","\\\\")+"\""
            if index < len(cmds)-1:
                cmd+=','
        cmd+=")"
        exec(cmd)
    except Exception as e:
        color.printRed('[-] Error.')
        color.printRed(str(e))
        try:
            exec(cmds[1]+".info()")
        except Exception as exc:
            color.printRed(str(exc))
            color.printRed('[-] Bad module.')
def make_list(command,commands):
    for library in libraries:
        color.printGreen(library)


def search_module(command, commands):
    try:
        find_list = []
        keywords = command.split()
        if len(keywords) <= 1:
            color.printGreen('Usage: search [KEYWORD]')
            color.printGreen('Example: search command')
            return -1
        for library in libraries:
            for key in range(1,len(keywords)):
                if (keywords[key] in library or library in keywords[key]) and library not in find_list:
                    find_list.append(library)
        for library in find_list:
            color.printGreen(library)
        return 0
    except:
        color.printGreen('Usage: search [KEYWORD]')
        color.printGreen('Example: search command')
        return -1


def server(command,commands):
    encryption = False
    try:
        cmds = str(command).split()
        host = cmds[1]
        port = cmds[2]
        password = cmds[3]
        hash_tool = hashlib.md5()
        hash_tool.update(password.encode())
        md5=hash_tool.hexdigest()
    except:
        color.printRed('Usage: server [IP/HOST] [PORT] [PASSWORD]')
        return -1
    try:
        service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        service.bind((host, int(port)))
        service.listen(5)
    except:
        print('Error.')
        return -1
    while True:
        try:
            client, addr = service.accept()
            service_status=True
            sys.stdout = r
            res = client.recv(71296).decode('gbk').lower()
            if res == md5.lower() or md5.lower() in res:
                sys.stdout = current
                color.printGreen(str(addr) + ' connected.')
                sys.stdout = r
                client.send('Welcome! Pervise Beta:)'.encode())
                while True:
                    try:
                        command = client.recv(71296).decode('gbk')
                        if command.lower() == "exit":
                            client.send('Goodbye! Pervise Beta:)'.encode())
                            client.close()
                            sys.stdout = current
                            color.printGreen(str(addr) + ' disconnected.')
                            service_status=False
                            break
                        if encryption:
                            command = dectry(command,md5)
                        sys.stdout = current
                        color.printGreen(str(addr) + ': '+str(command))
                        sys.stdout = r


                        if 'encrypt' in command.lower():
                            try:
                                if encryption == False:
                                    sys.stdout = current
                                    color.printYellow(str(addr) + ': Requesting encryption to server.')
                                    client.send(md5.encode())
                                    color.printGreen(str(addr) + ': The server can use encryption.')
                                    encryption = True
                                    color.printGreen(str(addr) + ': encryption -> True')
                                    sys.stdout = r
                                else:
                                    client.send(md5.encode())
                            except:
                                sys.stdout = current
                                color.printRed('[-] Error.')
                                sys.stdout = r
                                return -1
                            continue
                        elif 'decrypt' in command.lower():
                            try:
                                if encryption == True:
                                    sys.stdout = current
                                    color.printYellow(str(addr) + ': Requesting decryption to server.')
                                    encryption = False
                                    color.printGreen(str(addr) + ': encryption -> False')
                                    sys.stdout = r
                            except:
                                pass
                            continue
                        commands.get(command.split()[0].lower())(command, commands)
                        #"The command has been executed. To obtain the output information, log in to the server."
                        if encryption:
                            sys.stdout = current
                            #print(enctry(r.content, md5).encode())
                            sys.stdout = r
                            client.send(enctry(r.content, md5).encode())
                        else:
                            client.send(r.content.encode())
                        r.flush()
                    except:
                        if encryption:
                            client.send(enctry("[-] Bad command. Pervise Beta :(", md5).encode())
                        else:
                            client.send("[-] Bad command. Pervise Beta :(".encode())
        except:
            print('Error.')
            return -1

def connect(command,commands):
    encryption = False
    try:
        cmds = str(command).split()
        host = cmds[1]
        port = cmds[2]
        password = cmds[3]
        hash_tool = hashlib.md5()
        hash_tool.update(password.encode())
        md5=hash_tool.hexdigest()
    except:
        color.printRed('Usage: connect [IP/HOST] [PORT] [PASSWORD]')
        return -1
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((host, int(port)))
        server.settimeout(3)
        server.send(md5.encode())
        res = server.recv(1024).decode('gbk')
        color.printGreen(res)
        color.printGreen('[*] Use the encrypt command to manage encryption.')
        while True:
            command = input("(" + str(host) + ")Pervise> ")
            if command.lower() == "exit":
                server.send('exit'.encode())
                res = server.recv(1024).decode('gbk')
                server.close()
                color.printGreen(res)
                return 0
            elif 'settimeout' in command.lower():
                try:
                    server.settimeout(int(command.split()[1]))
                except:
                    color.printRed('[-] Error. Example: settimeout 5')
                    server.settimeout(3)
                continue
            elif 'make' in command.lower() and server.gettimeout() < 30:
                color.printYellow('[!] Creating Payload on the server requires some waiting time. We recommend that you set the timeout to more than 30 seconds.')
                color.printYellow('[!] If you use the listening module (such as the listen module of command_reverse_tcp), it will not work properly. Because your input could not be redirected to the server.')
                color.printGreen('[*] Command: settimeout 30')
            elif 'encrypt' in command.lower():
                try:
                    if 'true' in command.lower().split()[1]:
                        color.printYellow('[!] Requesting encryption to server.')
                        server.send('encrypt'.encode())
                        res = server.recv(1024).decode('gbk')
                        if md5.lower() in res.lower():
                            color.printGreen('[*] The server can use encryption.')
                            encryption = True
                        else:
                            color.printRed('[-] The server does not support encryption. It may be caused by the server software or the wrong password.')
                    elif 'false' in command.lower().split()[1]:
                        color.printYellow('[!] Requesting the server to stop encryption.')
                        server.send(enctry('decrypt',md5).encode())
                        color.printGreen('[*] Done.')
                        encryption = False
                except:
                    color.printRed('[-] Error.')
                    color.printGreen('[*] Usage: encrypt true/false')
                continue

            #commands.get(command.split()[0].lower())(command, commands)
            if encryption:
                server.send(enctry(command,md5).encode())
                res = dectry(server.recv(65536).decode('gbk'),md5)
            else:
                server.send(command.encode())
                res = server.recv(8192).decode('gbk')
            print(res)

    except:
        color.printRed('[-] The server is not responding or the token is incorrect.')
        return -1


def start_server(command,commands):
    t = threading.Thread(target=server,args=(command,commands,),daemon=True)
    t.start()

def wget(command,commands):
    cmds = command.split()
    try:
        url = cmds[1]
        path = cmds[2]

        filename = url[url.rindex('/') + 1:]
        print('filename = ' + filename)

        downloaded = '0'

        def download_listener(a, b, c):
            per = 100.0 * a * b / c
            if per > 100:
                per = 100
            new_downloaded = '%.1f' % per
            nonlocal downloaded
            if new_downloaded != downloaded:
                downloaded = new_downloaded
                color.printGreen('download %s%%  %s/%s' % (downloaded, a * b, c))

        if not os.path.exists(path):
            os.mkdir(path)

        response = urllib.request.urlretrieve(url, path + filename, download_listener)
    except Exception as e:
        color.printRed('[-] Failed.')
        color.printRed(str(e))
        color.printGreen('Usage: wget [URL] [SAVE PATH]')
        color.printGreen('Example: wget http://103.103.14.1/pervise.py D:\\')

def curl(command,commands):
    cmds = command.split()
    try:
        url = cmds[1]
    except:
        color.printGreen('Usage: curl [URL]')
        return -1
    try:
        result = requests.get(url)
        color.printYellow("Code: "+str(result.status_code()))
        color.printGreen("Headers: ")
        print(result.headers())
        color.printRed("Content: ")
        print(str(result.content))
    except Exception as e:
        color.printRed('[-] Failed.')
        color.printRed(str(e))
        return -1

def run_command(command,commands):
    cmds = command.split()
    statement = ""
    for index in range(1,len(cmds)):
        statement+=cmds[index]+' '
    p = subprocess.Popen(statement, shell=True, stdout=subprocess.PIPE)
    while p.poll() is None:
        if p.wait() is not 0:
            color.printRed('[-] Bad system command.')
            return -1
        else:
            re = p.stdout.readlines()
            result = []
            for i in range(len(re)):
                res = re[i].decode('gbk').strip('\r\n')
                result.append(res)
            for line in result:
                print(line)
            return -1

def exec_command(command,commands):
    cmds = command.split()
    cmd = ''
    try:
        for index in range(1,len(cmds)):
            cmd+=cmds[index]+' '
        exec(cmd)
        return 0
    except Exception as e:
        color.printRed(str(e))
        return -1
