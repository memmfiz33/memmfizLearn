# 1. Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля, отмеченные символом *
# : First name, last name, email. Текст для полей может быть любым.
# 2. Успешность регистрации проверяется сравнением ожидаемого текста "Congratulations! You have successfully registered!"
# с текстом на странице, которая открывается после регистрации. Для сравнения воспользуемся стандартной конструкцией assert из языка Python.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/registration1.html"

with webdriver.Chrome () as driver:
    driver.get(link)


    req_inputs = driver.find_elements(By.CSS_SELECTOR, "input[required]")
    for req in req_inputs:
        req.send_keys("Test_data")

#    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    time.sleep(2)

    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert welcome_text == "Congratulations! You have successfully registered!"
    print("Successfully registered!")
