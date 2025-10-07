from selenium.webdriver.common.by import By
import pytest

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser_select):
    browser_select.get(link)
    browser_select.find_element(By.CSS_SELECTOR, "#login_link")
