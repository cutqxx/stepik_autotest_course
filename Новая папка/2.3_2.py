from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

try:
    browser.find_element_by_tag_name('button').click()
    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x_el = browser.find_element_by_id("input_value").text
    x = calc(x_el)
    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(x)
    browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(10)
    browser.quit()