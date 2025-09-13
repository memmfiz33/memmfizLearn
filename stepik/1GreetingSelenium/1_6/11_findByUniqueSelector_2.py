from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "https://suninjuly.github.io/registration2.html"

with webdriver.Chrome () as driver:
    driver.get(link2)

    fn_input = driver.find_element(By.CSS_SELECTOR, ".first_block .first")
    fn_input.send_keys("Ivan")

    ln_input = driver.find_element(By.CSS_SELECTOR, ".first_block .second")
    ln_input.send_keys("Petrov")

    e_input = driver.find_element(By.CSS_SELECTOR, ".first_block .third")
    e_input.send_keys("piemail@mail.com")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")

    time.sleep(2)
    button.click()
    time.sleep(2)

    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Congratulations! You have successfully registered!"

    print("Successfully registered!")

