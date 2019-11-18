import pyautogui
import time
import subprocess
from screenshot import take_screenshot

CHROME_LOCATION = [612, 1055]
STUDY_ROOM_LINK_LOCATION = [655, 84]


def click(coordinates):
    pyautogui.click(coordinates[0], coordinates[1])


def locate_button(image):
    read_img = pyautogui.locateCenterOnScreen(image)
    click(read_img)


def isValid():
    for i in range(760, 1525, 27):
        for j in range(580, 811, 27):
            x = pyautogui.pixelMatchesColor(i, j, (20, 149, 31))
            pyautogui.moveTo(i, j)
            if x:
                time.sleep(0.5)
                pyautogui.leftClick(i, j)
                return


def click_down_arrow():
    img = list(pyautogui.locateAllOnScreen("down_arrow.png"))
    click(img[-1])
    return img[-1]


def run():
    time.sleep(3)
    chrome_browser = subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    time.sleep(3)
    click(STUDY_ROOM_LINK_LOCATION)
    time.sleep(5)
    locate_button('8peopleroom.png')
    time.sleep(3)
    isValid()
    time.sleep(2)
    down_arrow_location = click_down_arrow()
    time.sleep(2)
    pyautogui.leftClick(down_arrow_location[0], down_arrow_location[1] + (15 * 6))
    time.sleep(2)
    locate_button("submit_times.png")
    time.sleep(2)
    pyautogui.scroll(-100000)
    time.sleep(1)
    locate_button("continue.png")
    time.sleep(3)
    locate_button("first_name.png")
    time.sleep(1)
    pyautogui.typewrite("Rijan")
    time.sleep(2)
    locate_button("last_name.png")
    time.sleep(1)
    pyautogui.typewrite("Timsina")
    time.sleep(2)
    pyautogui.leftClick(720, 590)
    time.sleep(1)
    pyautogui.typewrite("rtimsin@gmu.edu")
    time.sleep(2)
    locate_button("submit_my_booking.png")
    time.sleep(2)


run()
