# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

url = "http://suninjuly.github.io/explicit_wait2.html"
target_price = "100"

# open the page
with webdriver.Chrome() as driver:
    driver.get(url)

    #wait for the required price
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), target_price)
    )
    #click on book btn when the price == target_price
    book_btn = driver.find_element(By.ID, "book")
    book_btn.click()

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
