from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("someone")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("someone")
    email = browser.find_element_by_name("email")
    email.send_keys("someone")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    add_file = browser.find_element_by_id("file")
    add_file.send_keys(file_path)
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
