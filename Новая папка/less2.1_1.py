import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x_el = browser.find_element_by_id("treasure")
    x = x_el.get_attribute("valuex")
    y = calc(x)
    print(x)
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys(y)

    browser.find_element_by_id('robotCheckbox').click()

    option1 = browser.find_element_by_css_selector("[value='robots']")
    option1.click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()