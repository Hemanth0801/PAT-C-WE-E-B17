import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
    def open_url(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self,username,password):
        self.driver.find_element(By.ID,'user-name').send_keys(username)
        self.driver.find_element(By.ID,'password').send_keys(password)
        self.driver.find_element(By.XPATH,'//input[@class="submit-button btn_action"]').click()
        time.sleep(2)

    def get_title(self):
        title = self.driver.title
        return title

    def get_url(self):
        url = self.driver.current_url
        return url

    def save_page_content(self):
        content = self.driver.page_source
        with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
            file.write(content)
        print("page content saved")

    def close_browser(self):
        self.driver.quit()

obj = LoginPage(driver)
obj.open_url()
obj.login("standard_user", "secret_sauce")
obj.get_title()
obj.get_url()
obj.save_page_content()
obj.close_browser()





