from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
import math
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    n1 = browser.find_element(By.ID, "num1")
    n2 = browser.find_element(By.ID, "num2")
    nx =int(n1.text) + int(n2.text)
    nx=str(nx)
    print(nx)
    res = browser.find_element(By.CSS_SELECTOR,f'[value="{nx}"]')
    browser.find_element(By.CSS_SELECTOR, f'[value="{nx}"]').click()
    print(f'[value="{nx}"]')
    print(res.text)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()