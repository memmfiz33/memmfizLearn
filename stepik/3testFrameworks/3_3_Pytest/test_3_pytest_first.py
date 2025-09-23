from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

SUCCESS_TEXT = "Congratulations! You have successfully registered!"

def fill_and_submit (driver, url):
    driver.get(url)
    driver.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
    driver.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
    driver.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("piemail@mail.com")
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    h1 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )
    return h1.text

@pytest.mark.parametrize("url", [
    "http://suninjuly.github.io/registration1.html",
    "http://suninjuly.github.io/registration2.html",
])

def test_registration(url):
    with webdriver.Chrome() as driver:
        assert fill_and_submit(driver, url) == SUCCESS_TEXT

if __name__ == "__main__":
    pytest.main()
