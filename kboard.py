from pynput.keyboard import Key, Controller
import time
import random

kb = Controller()

time.sleep(3)
#Please run
# ---------- Anti Bot Detection ----------

# random flat between a and b 
def rand(a, b):
    base = random.randint(a, b)
    return round(base)
time.sleep(1)
print("Start")


# ---------------- Moves -----------------
#   Face the pokemon center before the voctory road and start the program

def heal():
    "Start Healing"
    kb.press("w")
    time.sleep(rand(10, 13))
    kb.release("w")

def exit_poke_center_1(): #Create a second one to avoid the bot detection (change the inputs)
    "Exit the Poke Center"
    kb.press(Key.down)
    time.sleep(2)
    kb.release(Key.down)
    time.sleep(0.2)

def run_2_cave():
    "Run to the cave"
    n = random.randint(7,9)
    print(n)
    for i in range(n):
        kb.press(Key.right)
        time.sleep(0.2)
        kb.release(Key.right)
    kb.press(Key.up)
    time.sleep(1)
    kb.release(Key.up)
    time.sleep(1)
    kb.press(Key.up)
    time.sleep(0.2)
    kb.release(Key.up)

def use_move():
    kb.press("-")
    time.sleep(0.2)
    kb.release("-")
    time.sleep(15)

def encounter():
    time.sleep(0.2)
    for i in range(3):
        kb.press("w")
        time.sleep(0.3)
        kb.release("w")

def back_to_pokecenter():
    kb.press(Key.down)
    time.sleep(3)
    kb.release(Key.down)
    time.sleep(0.2)
    kb.press(Key.left)
    time.sleep(1.6)
    kb.release(Key.left)
    time.sleep(0.2)
    kb.press(Key.up)
    time.sleep(3)
    kb.release(Key.up)


def main():
    while True:
        heal()
        time.sleep(0.2)
        exit_poke_center_1()
        time.sleep(0.2)
        run_2_cave()
        for i in range(4):
            time.sleep(3)
            use_move()
            time.sleep(1)
            encounter()
            time.sleep(1)
        back_to_pokecenter()
        time.sleep(0.2)

        print("ca repart")
if __name__ == "__main__":
    main()