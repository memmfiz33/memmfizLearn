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
    # click ENTER button
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    ).click()

    #Authorization (login and password input than submit)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "id_login_email"))
    ).send_keys(LOGIN)
    browser.find_element(By.ID, "id_login_password").send_keys(PASSWORD)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

    browser.get(url)

    #add answer and click submit
    answer = str(math.log(int(time.time())))
    answer_field = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.string-quiz__textarea, .CodeMirror textarea"))
    )
    answer_field.clear()
    answer_field.send_keys(answer)

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    ).click()

    answer_text = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    ).text.strip()

    assert answer_text == ("Correct!", f"EXPECTED: 'Correct!', ACTUAL: {answer_text!r}")
    time.sleep(3)







