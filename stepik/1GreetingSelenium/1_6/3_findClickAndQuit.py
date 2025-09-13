from selenium import webdriver
from selenium.webdriver.common.by import By
import time



# try: ##
#     link = "http://suninjuly.github.io/simple_form_find_task.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     time.sleep(5)
#     button.click()
#
# finally:
#     browser.quit()

with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    time.sleep(1)
    button.click()