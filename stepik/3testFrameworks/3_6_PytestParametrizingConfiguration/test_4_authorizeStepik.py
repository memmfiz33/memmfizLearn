import pytest
from selenium import webdriver
import math
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()
LOGIN = os.environ["stepik_login"]
PASSWORD = os.environ["stepik_password"]
URLS = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.mark.parametrize("url", URLS)
def test_authorized_browser(browser, url):
    browser.get(url)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "ember484"))
    ).click()

    #Authorization (login and password input than submit)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "id_login_email"))
    ).send_keys(LOGIN)
    browser.find_element(By.ID, "id_login_password").send_keys(PASSWORD)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

    #click submit
    browser.find.element(By.CSS_SELECTOR,"button.submit-submission[type='button']").click()
    answer = math.log(int(time.time()))
    print(answer)
    time.sleep(3)







