import os
import time

from selenium import webdriver

projectpath = os.path.dirname(os.path.dirname(os.getcwd()))

browserName = "Firefox"
webdriver.driver = None

if browserName == "Chrome":
    driver = webdriver.Chrome(executable_path=projectpath+"/browser_drivers/chromedriver")
elif browserName == "Firefox":
    driver = webdriver.Firefox(executable_path=projectpath + "/browser_drivers/geckodriver")
elif browserName == "Edge":
    driver = webdriver.Edge(executable_path=projectpath + "/browser_drivers/msedgedriver")
else:
    print("Browser name was not given....")

try:
    driver.get("https://www.facebook.com")
    time.sleep(5)
    driver.quit()
except NameError as error:
    print(error)


