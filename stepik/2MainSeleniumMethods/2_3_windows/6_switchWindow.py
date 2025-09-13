# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/redirect_accept.html"

with webdriver.Chrome() as driver:
    driver.get(url)

    # click on flying button
    flying_submit  = driver.find_element(By.XPATH, '//button[@type="submit"]')
    flying_submit.click()
    time.sleep(1)

    # switch to second tab
    new_window = driver.window_handles[1]
    current_window = driver.window_handles[0]
    driver.switch_to.window(new_window)
    time.sleep(1)

    # find and calculate x element
    x_elem = driver.find_element(By.ID, 'input_value')
    x = int(x_elem.text)
    def calc(x):
        return math.log(abs(12 * math.sin(x)))
    y = str(calc(x))

    # input answer
    input_value = driver.find_element(By.ID, 'answer')
    input_value.send_keys(y)

    # click submit button
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()
    time.sleep(10)
