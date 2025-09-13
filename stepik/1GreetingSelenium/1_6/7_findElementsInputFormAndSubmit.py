from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"

with webdriver.Chrome() as driver:
    driver.get(link)

    elements = driver.find_elements(By.TAG_NAME, "input")
    for el in elements:
        el.send_keys("test")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(30)
