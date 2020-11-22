import pyautogui, time, random

time.sleep(2)
f = open("beemovie", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(random.randint(3, 10))