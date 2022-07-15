# compatible with major apps (ig, discord)


import pyautogui
import time

f = open("message.txt", "r+")
pyautogui.click(x=1158, y=858)


try:
    for i in range(9999):
        pyautogui.write(next(f), interval=0)
        pyautogui.press('enter')
        # time.sleep(0.2)

except StopIteration:
    pass

f.close()