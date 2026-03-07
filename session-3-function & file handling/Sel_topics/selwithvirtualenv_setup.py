import time
from logging import raiseExceptions
from operator import truediv
from sys import exception

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Browser:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def __init__(self,url):
        self.url = url
    def launch_application(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            return True
        except exception as e:
            print("not found")
            return False

    def get_title(self):
        if self.launch_application():
            return self.driver.title
        else:
            raise Exception ("error")

    def login_(self):
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(2)
        self.driver.save_screenshot("screenshot.png")

    def close_browser(self):
        self.driver.quit()

if __name__ == "__main__":
    url='https://www.guvi.in/'
    my_browser = Browser(url)
    my_browser.launch_application()
    title_of_the_page = my_browser.get_title()
    if title_of_the_page == "HCL GUVI | Learn to code in your native language":
            print("Passed")
    else:
        print("Failed")
    # url_of_page = my_browser.url
    # if url_of_page  == url:
    #     print("Passed")
    # else:
    #     print("Failed")
    # time.sleep(2)
    # my_browser.close_browser()

# driver.get('https://www.guvi.in/')
