from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    summa = int(num1) + int(num2)
    summa = str(summa)
    print(summa)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summa)

    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()
    # пустая строка