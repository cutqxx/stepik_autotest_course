from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не станет = 100
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )

browser.find_element_by_css_selector('button#book').click()
x_el = browser.find_element_by_id("input_value").text
x = calc(x_el)
input1 = browser.find_element_by_css_selector("input#answer")
input1.send_keys(x)
browser.find_element_by_css_selector('button#solve').click()

time.sleep(10)
browser.quit()
