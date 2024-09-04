from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    valx=browser.find_element(By.ID, "treasure")
    valx = valx.get_attribute("valuex")
    valx = calc(valx)
    res=browser.find_element(By.ID, "answer")
    res.send_keys(valx)
    rescheck = browser.find_element(By.ID, "robotCheckbox")
    rescheck.click()
    robotcheck = browser.find_element(By.ID, "robotsRule")
    robotcheck.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()