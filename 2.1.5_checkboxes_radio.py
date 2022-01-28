from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"
browser.get(link)

try:
    x_element = browser.find_element_by_css_selector('img#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(y)
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    box = browser.find_element_by_id('robotsRule')
    box.click()
    option = browser.find_element_by_css_selector("button.btn")
    option.click()

finally:
    time.sleep(10)
    browser.quit()
