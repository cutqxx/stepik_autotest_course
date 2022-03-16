from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
try:

    x_el = browser.find_element_by_id("input_value").text
    x = calc(x_el)

    # --

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)

    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(x)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_css_selector('[value="robots"]').click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()
#-----