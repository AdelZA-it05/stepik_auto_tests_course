from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    valx=browser.find_element(By.ID, "input_value")
    valx =calc(valx.text)
    res=browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", res)
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