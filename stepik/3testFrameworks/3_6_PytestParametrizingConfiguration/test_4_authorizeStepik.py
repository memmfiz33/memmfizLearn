import os
import time
import math
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    time.sleep(1)
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize("url", URLS)
def test_authorized_browser(browser, url):
    browser.get(url)
    time.sleep(1)

    # click ENTER button
    WebDriverWait(browser, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))).click()

    time.sleep(1)
    #Authorization (login and password input than submit)
    WebDriverWait(browser, 7).until(EC.element_to_be_clickable((By.ID, "id_login_email"))).send_keys(LOGIN)
    browser.find_element(By.ID, "id_login_password").send_keys(PASSWORD)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

    # add a pause
    WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "a.navbar__auth_login")))

    # return to the target page
    browser.get(url)

    try:
        retry_button = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.again-btn.white"))
        )
        if retry_button.is_displayed() and retry_button.is_enabled():
            print("[INFO] Click 'Решить снова' button. Skip the step")
            retry_button.click()
            WebDriverWait(browser, 5).until_not(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.again-btn.white"))
            )
    except:
        print("[INFO] No 'Решить снова' button, continue...")

    #add answer and click submit
    answer = str(math.log(int(time.time())))
    answer_field = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.string-quiz__textarea, .CodeMirror textarea"))
    )
    answer_field.clear()
    answer_field.send_keys(answer)


    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    ).click()

    answer_text = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    ).text.strip()
    print(f"ANSWER: {answer_text}")

    assert answer_text == "Correct!", f"EXPECTED: 'Correct!', ACTUAL: {answer_text!r}"
    time.sleep(1)

