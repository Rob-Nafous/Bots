import pyautogui as pg, sys, time, random

# ---------- Anti Bot Detection ----------

# random flat between a and b 
def rand(a, b):
    base = random.randint(a, b)
    return round(base)
time.sleep(2)
print("Start")


# ---------------- Moves -----------------
#   Face the pokemon center before the voctory road and start the program

def heal():
    
    return True

# Heal pokemon and exit the Poke Center
def exit_poke_center():
    pg.moveTo(387, 227, 0.5)
    pg.press("z")
    time.sleep(3)
    for i in range(9):
        time.sleep(1)
        if i > 4:
            pg.leftClick()
            time.sleep(1)
        else:
            pg.press("z")
            time.sleep(1)
        time.sleep(1.5)
    time.sleep(1)
    pg.keyDown('down')
    time.sleep(rand(1.7,2.0))
    pg.keyUp('down')
    time.sleep(rand(1.2,1.3))
    pg.press('down')
    pg.keyDown('down')
    time.sleep(0.2)
    pg.keyUp('down')
    time.sleep(rand(1,1))
    pg.press('3')
    time.sleep(rand(1,1))

# Walk towards the waterfall and surf
def go_to_waterfall():
    pg.keyDown('right')
    time.sleep(rand(2,2))
    pg.keyUp('right')
    time.sleep(rand(1,1))
    pg.keyDown('down')
    time.sleep(rand(1,1))
    pg.keyUp('down')
    time.sleep(rand(1,1))
    pg.press('3')
    time.sleep(rand(1,1))
    pg.keyDown('up')
    time.sleep(0.2)
    pg.keyUp('up')
    time.sleep(rand(1,2))
    pg.press('right')
    time.sleep(2)
    pg.keyDown('right')
    time.sleep(rand(1,1))
    pg.keyUp('right')
    time.sleep(rand(1,1))
    pg.keyDown('down')
    time.sleep(0.5)
    pg.keyUp('down')
    time.sleep(random.randint(1,2))
    pg.press('5')
    time.sleep(rand(1,1))

# Start Encounter
def farm():
    for i in range(6):
        time.sleep(1)
        pg.press('6')
        time.sleep(rand(14,15))
        pg.press('z')
        time.sleep(rand(0.2,0.5))
        pg.press('z')
        time.sleep(rand(0.2,0.5))
        pg.press('z')
        time.sleep(rand(6,7))
    pg.press('2')
    time.sleep(random.randint(1,2))

# Starting of program
def main():
    pg.moveTo(387, 227, 0.5)
    pg.leftClick()

    while(True):
        exit_poke_center()
        go_to_waterfall()
        farm()

if __name__ == "__main__":
    main()