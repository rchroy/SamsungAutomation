from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser


    def getWebDriverInstance(self):
        url = "https://www.samsung.com/in/smartphones/galaxy-z/"
        if self.browser == 'chrome':
            option1 = Options()
            option1.add_argument("--disable-notifications")
            option1.add_argument("start-maximized")
            driver = webdriver.Chrome(options=option1)
            driver.get(url)
            driver.implicitly_wait(3)
            return driver

        elif self.browser == 'firefox':
            driver = webdriver.Firefox()
            driver.fullscreen_window()
            driver.get(url)
            driver.implicitly_wait(3)
            return driver

        else:
            print("Sorry Currently this browser is not supported")
