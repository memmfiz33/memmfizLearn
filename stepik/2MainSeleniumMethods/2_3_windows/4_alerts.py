# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/alert_accept.html"

# Open the link
with webdriver.Chrome() as driver:
    driver.get(url)

    # click on start button
    start_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    start_button.click()

    # click on confirm button
    confirm = driver.switch_to.alert
    confirm.accept()
    time.sleep(1)
    # find and store x value
    x_elem = driver.find_element(By.ID, 'input_value')
    x = int(x_elem.text)


    # calculate math formula
    def calc(x):
        return math.log(abs(12 * math.sin(x)))
    y = str(calc(x))


    # input answer
    input_field = driver.find_element(By.ID, 'answer')
    input_field.send_keys(y)

    # click submit button
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()
    time.sleep(10)
