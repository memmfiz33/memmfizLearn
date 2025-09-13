# Открыть страницу https://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "https://suninjuly.github.io/execute_script.html"


with webdriver.Chrome() as driver:
    driver.get(url)
    time.sleep(1)

    x_elem = driver.find_element(By.XPATH, '//label/span[@id="input_value"]')
    x = int(x_elem.text)

    def calc(x):
        return math.log(abs(12 * math.sin(x)))

    y = str(calc(x))

    input_element = driver.find_element(By.ID, 'answer')
    input_element.send_keys(y)

    checkbox = driver.find_element(By.ID, 'robotCheckbox')
    if not checkbox.is_selected():
        driver.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
        checkbox.click()

    radioButton = driver.find_element(By.ID, 'robotsRule')
    if not radioButton.is_selected():
        driver.execute_script("return arguments[0].scrollIntoView(true);", radioButton)
        radioButton.click()

    submit_button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    time.sleep(3)





