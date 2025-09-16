from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/cats.html"

with webdriver.Chrome() as driver:
    driver.get(url)
    driver.find_element(By.ID, "button")