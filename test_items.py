from selenium.webdriver.common.by import By
import time

def test_check_add_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket" ), "The button not found!"