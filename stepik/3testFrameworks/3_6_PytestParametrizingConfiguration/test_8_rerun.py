from selenium.webdriver.common.by import By
import pytest

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser_select):
    browser_select.get(link)
    browser_select.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser_select):
    browser_select.get(link)
    browser_select.find_element(By.CSS_SELECTOR, "#magic_link")