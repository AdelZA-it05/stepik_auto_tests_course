from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, "firstname").send_keys("firstname")
    browser.find_element(By.NAME, "lastname").send_keys("lastname")
    browser.find_element(By.NAME, "email").send_keys("email")
    file_path = os.path.join('C:\PythonProjects\MyPythonProjects', 'qqq.txt')
    browser.find_element(By.NAME, "file").send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()