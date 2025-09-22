from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
SUCCESS_TEXT = "Congratulations! You have successfully registered!"

class TestAbs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def fill_and_submit(self, link):
        driver = self.driver
        driver.get(link)

        fn_input = driver.find_element(By.CSS_SELECTOR, ".first_block .first")
        fn_input.send_keys("Ivan")

        ln_input = driver.find_element(By.CSS_SELECTOR, ".first_block .second")
        ln_input.send_keys("Petrov")

        e_input = driver.find_element(By.CSS_SELECTOR, ".first_block .third")
        e_input.send_keys("piemail@mail.com")

        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        return welcome_text_elt.text

    def test_registration1(self):
        text = self.fill_and_submit(link1)
        self.assertEqual(text, SUCCESS_TEXT, "Registration1 failed")

    def test_registration2(self):
        text = self.fill_and_submit(link2)
        self.assertEqual(text, SUCCESS_TEXT, "Registration2 failed")


if __name__ == "__main__":
    unittest.main()
