from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

try:
    browser.find_element_by_class_name("btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x))
    browser.find_element_by_class_name("btn").click()
    answer = browser.switch_to.alert
    print(answer.text.split()[-1])

finally:
    browser.quit()
