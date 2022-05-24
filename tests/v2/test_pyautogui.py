import pyautogui
import keyboard
import time
import PIL

# Grid = 10 x 8
width, height = pyautogui.size()
ss = pyautogui.screenshot("out.png")
mode = input("Mode (small/medium): ").lower()
cellpx = 45 if mode == "small" else 30
if mode == "small":
    sx, sy = 473, 305
else:
    sx, sy = 418, 269
pyautogui.moveTo(sx, sy)
pyautogui.click()

def screenshot() -> None:
    pyautogui.screenshot("out.png")

def position() -> None:
    print(pyautogui.position())
    time.sleep(0.1)

def start() -> None:
    pyautogui.moveTo(sx, sy)
    pyautogui.click()

def up() -> None:
    global x
    global y
    y -= cellpx
    pyautogui.moveTo(x, y)

def down() -> None:
    global x
    global y
    y += cellpx
    pyautogui.moveTo(x, y)

def left() -> None:
    global x
    global y
    x -= cellpx
    pyautogui.moveTo(x, y)

def right() -> None:
    global x
    global y
    x += cellpx
    pyautogui.moveTo(x, y)

keyboard.add_hotkey("s", screenshot)
keyboard.add_hotkey("p", position)
keyboard.add_hotkey("g", start)
keyboard.add_hotkey("up", up)
keyboard.add_hotkey("down", down)
keyboard.add_hotkey("left", left)
keyboard.add_hotkey("right", right)
keyboard.add_hotkey("f", pyautogui.rightClick)
keyboard.add_hotkey("c", pyautogui.click)
keyboard.add_hotkey("q", quit)

while True:
    x, y = pyautogui.position()