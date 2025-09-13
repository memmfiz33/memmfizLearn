# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"

with webdriver.Chrome() as driver:
    driver.get(link)
    time.sleep(2)

    treasure_image = driver.find_element(By.ID, "treasure")
    treasure_attribute = treasure_image.get_attribute("valuex")
    assert treasure_attribute is not None, "valuex attribute not found"

    x = treasure_attribute

    def calc(treasure_attribute: str) -> str:
         x = float(treasure_attribute)
         return str(math.log(abs(12 * math.sin(x))))
    y = calc(x)

    input_element = driver.find_element(By.ID, "answer")
    input_element.send_keys(y)
    time.sleep(2)

    checkbox = driver.find_element(By.ID, "robotCheckbox")
    if not checkbox.is_selected():
        checkbox.click()
    time.sleep(2)

    radiobutton = driver.find_element(By.ID, "robotsRule")
    if not radiobutton.is_selected():
        radiobutton.click()
    time.sleep(2)

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    time.sleep(10)



