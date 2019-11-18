import pyautogui
import time


def take_screenshot():
    img = pyautogui.screenshot()
    img.save("screenshot.png")


if __name__ == "__main__":
    for i in range(5, 1, -1):
        print(i)
    take_screenshot()
