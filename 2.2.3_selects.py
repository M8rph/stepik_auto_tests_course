from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

try:
    num1 = browser.find_element_by_css_selector('h2 :nth-child(2)')
    num2 = browser.find_element_by_css_selector('h2 :nth-child(4)')
    num_sum = str(int(num1.text) + int(num2.text))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(num_sum)

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
