import ctypes
import threading
import time

word = chr(1089)+chr(1080)+chr(1087)+chr(1077)+chr(1089)+chr(1090)+chr(1072)+chr(1090)+' '+chr(1087)+chr(1080)+chr(1076)+chr(1088)
running = True

def show():
    try:
        ctypes.windll.user32.MessageBoxTimeoutW(0, word, 'ОШИБКА СИСТЕМЫ', 0x10, 0, 0)
    except:
        pass

def loop():
    while running:
        threading.Thread(target=show).start()
        time.sleep(0.1)

threading.Thread(target=loop).start()
try:
    while 1: time.sleep(1)
except:
    running = False
