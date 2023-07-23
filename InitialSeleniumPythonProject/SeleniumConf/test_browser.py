import selenium
from selenium import webdriver
import os

projectpath = os.path.dirname(os.path.dirname(os.getcwd()))
path = projectpath + "/browser_drivers/chromedriver"

# Windows user
# path = projectpath + "\\browser_drivers\\chromedriver"
# path = "C:\\Users\\anshul\selenium-python\\browser_drivers\\chromedriver.exe"

browser = webdriver.Chrome(executable_path=path)
browser.get("https://www.facebook.com")