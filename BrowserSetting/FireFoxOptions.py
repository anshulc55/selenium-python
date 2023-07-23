import time
from selenium import webdriver


def test_firefoxOptions():
    #FireFox Options
    f_options = webdriver.FirefoxOptions()
    f_options.headless = False
    f_options.accept_insecure_certs = False
    f_options.set_preference("dom.webnotifications.enabled", False)
    f_options.set_preference("browser.download.useDownloadDir", True)
    f_options.set_preference("browser.helperApps.alwaysAsk.force", False)
    f_options.add_argument("--height=880")
    f_options.add_argument("--width=1820")



    firefox = webdriver.Firefox(options=f_options)
    #firefox.maximize_window()
    firefox.get("https://www.facebook.com")
    time.sleep(5)
    firefox.quit()