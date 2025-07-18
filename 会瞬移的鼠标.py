import pyautogui
import random
import time

print("你的鼠标现在不受控制了！")
print("按Ctrl+C停止")

try:
    while True:
        x, y = pyautogui.position()
        new_x = x + random.randint(-100, 100)
        new_y = y + random.randint(-100, 100)
        pyautogui.moveTo(new_x, new_y, duration=0.1)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("好吧，还你控制权！")
