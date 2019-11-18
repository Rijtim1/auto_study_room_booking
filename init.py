from selenium import webdriver
import pyautogui
import time
from screenshot import take_screenshot

SEARCH_BOX = [760, 600, 1520, 970]


def find_empty_room(box):
    for i in range(box[0], box[2], 28):
        for j in range(box[1], box[3], 26):
            color_match = pyautogui.pixelMatchesColor(i, j, (20, 149, 31))
            pyautogui.moveTo(i, j)
            if color_match:
                time.sleep(0.5)
                a = pyautogui.pixelMatchesColor(i + 28, j, (20, 149, 31))
                if a:
                    pyautogui.leftClick(i, j)
                    return i, j


def press_down_arrow():
    for i in range(10):
        pyautogui.press('down')
        time.sleep(1)
    pyautogui.press('enter')


def find_next_week():
    for x in range(280, 605, 30):
        for y in range(320, 565, 30):
            color_match = pyautogui.pixelMatchesColor(x, y, (255, 219, 153))
            if color_match:
                pyautogui.leftClick(x + 30, y + 30)
                return x, y



DRIVER_PATH = r"C:\Users\rijan\Google Drive (stephneh18@gmail.com)\Python\chromedriver.exe"

driver = webdriver.Chrome(DRIVER_PATH)
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("https://library.gmu.edu/use/study-rooms")
time.sleep(2)
fenwick_six = driver.find_element_by_xpath(
    """//*[@id="node-38"]/div/div/div/div/table/tbody/tr[3]/td[3]/p[3]/a""")
fenwick_six.click()
go_to_date = driver.find_element_by_xpath("""//*[@id="eq-time-grid"]/div[1]/div[1]/button[1]""").click()
time.sleep(2)
find_next_week()
pyautogui.click(934, 951)
time.sleep(2)
find_empty_room(SEARCH_BOX)
pyautogui.scroll(-10000)
time.sleep(2)
room_option_selection = driver.find_element_by_xpath("""//*[@id="bookingend_1"]""").click()
press_down_arrow()
submit_button = driver.find_element_by_xpath("""//*[@id="submit_times"]""").click()
time.sleep(2)
pyautogui.scroll(-100000)
continue_button = driver.find_element_by_xpath("""//*[@id="terms_accept"]""").click()
time.sleep(2)
first_name = driver.find_element_by_xpath("""//*[@id="fname"]""").send_keys("Rijan")
last_name = driver.find_element_by_xpath("""//*[@id="lname"]""").send_keys("Timsina")
email = driver.find_element_by_xpath("""//*[@id="email"]""").send_keys("rtimsin@gmu.edu")
submit_my_booking = driver.find_element_by_xpath("""//*[@id="btn-form-submit"]""").click()
time.sleep(3)
driver.close()
