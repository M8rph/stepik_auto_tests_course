from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:
    button1 = browser.find_element_by_class_name("btn")
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    button2 = browser.find_element_by_class_name("btn")
    button2.click()
    alert = browser.switch_to.alert
    print(alert.text)

finally:
    browser.quit()
