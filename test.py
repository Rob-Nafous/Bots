from pynput.keyboard import Key, Controller
import time
import random

kb = Controller()

while True:
    for i in range(4):
        print("go")
        kb.press(Key.right)
        kb.release(Key.right)
