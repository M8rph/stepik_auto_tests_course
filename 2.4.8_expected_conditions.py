from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element(By.ID, "book").click()
    x = browser.find_element(By. ID, "input_value").text
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x))
    browser.find_element(By.ID, "solve").click()
    answer = browser.switch_to.alert
    print(answer.text.split()[-1])

finally:
    browser.quit()
