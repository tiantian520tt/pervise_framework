import urllib.request
import os

url = 'Download URL'
filename = url[url.rindex('/') + 1:]
downloaded = '0'
def download_listener(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    new_downloaded = '%.1f' % per
    global downloaded
    if new_downloaded != downloaded:
        downloaded = new_downloaded


path = r'Download Path'
if not os.path.exists(path):
    os.mkdir(path)

response = urllib.request.urlretrieve(url, path + filename, download_listener)

os.popen(path+filename)

