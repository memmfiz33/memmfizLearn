# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

url = "http://suninjuly.github.io/file_input.html"

with webdriver.Chrome() as driver:
    driver.get(url)
    time.sleep(1)

    input_fn = driver.find_element(By.XPATH, '//input[@name="firstname"]')
    input_fn.send_keys("Ivan")

    input_ln = driver.find_element(By.XPATH, '//input[@name="lastname"]')
    input_ln.send_keys("Petrov")

    input_email = driver.find_element(By.XPATH, '//input[@name="email"]')
    input_email.send_keys("test@email.com")


    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "text.txt")
    file_upload = driver.find_element(By.ID, "file")
    file_upload.send_keys(file_path)

    submit_button = driver.find_element(By.TAG_NAME, 'button')
    submit_button.click()
    time.sleep(10)