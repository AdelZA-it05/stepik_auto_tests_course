from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    valx=browser.find_element(By.ID, "input_value")
    valx =calc(int(valx.text))
    browser.find_element(By.ID, "answer").send_keys(valx)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()