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

with webdriver.Chrome () as driver:
    driver.get(link)
    time.sleep(1)

    x_el = driver.find_element(By.ID, "#input_value")
    x = x_el.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    cb_1 = driver.find_element(By.ID, "#robotCheckbox")
    cb_1.click()
    time.sleep(1)

    rb_2 = driver.find_element(By.ID, "#robotsRule")
    rb_2.click()
    time.sleep(1)

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    time.sleep(3)

