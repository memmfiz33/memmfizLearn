from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/simple_form_find_task.html"

with webdriver.Chrome() as driver:
    driver.get(link)

    value1 = "input"
    value2 = "last_name"
    value3 = "city"

    input1 = driver.find_element(By.TAG_NAME, value1)
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, value2)
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, value3)
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(30)



