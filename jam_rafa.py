import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print("⌚ JAM DIGITAL RAFA ⌚\n")
    print(time.strftime("%H:%M:%S"))
    time.sleep(1)