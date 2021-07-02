import pyautogui
import random
import os
from time import sleep
from copy import deepcopy
from dotenv import load_dotenv

load_dotenv()


SCROLL_SLEEP_TIME = int(os.getenv("SCROLL_SLEEP_TIME", 1))
SCROLL_DIRECTION = os.getenv("SCROLL_DIRECTION", "down")
SCROLL_DISTANCE = int(os.getenv("SCROLL_DISTANCE", 1))
HOT_KEYS = eval(os.getenv("HOT_KEYS", ['shift']))


pyautogui.hotkey(",".join(HOT_KEYS))


def run_gui():
    x, y = pyautogui.position()
    pyautogui.moveTo(x+random.randint(-10, 10), y+random.randint(-10, 10))
    # pyautogui.moveRel(0, 10)
    i = 0
    while i < random.randint(1, 10):
        # pyautogui.press(HOT_KEYS)
        key_choice = random.choice(HOT_KEYS)
        pyautogui.keyDown(key_choice)
        pyautogui.keyUp(key_choice)
        i += 1
    # screen_size = pyautogui.size()
    # current_screen_position = pyautogui.position()
    # pyautogui.scroll(1)


while True:
    try:

        run_gui()
        scroll_distance = deepcopy(SCROLL_DISTANCE)
        if SCROLL_DIRECTION.lower() == "down":
            scroll_distance = -1 * scroll_distance

        # for _ in range(random.randint(0, 4), random.randint(4, 7)):
        #     pyautogui.scroll(-1 * scroll_distance)
        #     pyautogui.scroll(scroll_distance)
        pyautogui.scroll(scroll_distance)
        sleep(SCROLL_SLEEP_TIME)
    except Exception as e:
        print(e)
        continue
