# Открыть страницу https://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

with webdriver.Chrome() as driver:
    driver.get(link)

    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    input_element = driver.find_element(By.ID, "answer")
    input_element.send_keys(y)
    time.sleep(1)

    checkbox_element = driver.find_element(By.ID, "robotCheckbox")
    if not checkbox_element.is_selected():
        checkbox_element.click()
    time.sleep(1)

    radioBut_element = driver.find_element(By.ID, "robotsRule")
    if not radioBut_element.is_selected():
        radioBut_element.click()
    time.sleep(1)

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    time.sleep(5)

