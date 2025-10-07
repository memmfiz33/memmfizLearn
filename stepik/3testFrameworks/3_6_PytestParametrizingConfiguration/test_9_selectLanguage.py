from selenium import webdriver
from selenium.webdriver.chrome.options import Options

user_language = {"ru", "en"}

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser1 = webdriver.Chrome(options=options)

fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser2 = webdriver.Firefox(firefox_profile=fp)