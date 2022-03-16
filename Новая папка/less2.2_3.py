from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
    browser.find_element_by_name('firstname').send_keys('имя')
    browser.find_element_by_name('lastname').send_keys('фамилия')
    browser.find_element_by_name('email').send_keys('test@gmail.com')
    browser.find_element_by_id('file').send_keys("/Users/siroja/Desktop/work/Без названия.txt")
    browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(10)
    browser.quit()
    # ---