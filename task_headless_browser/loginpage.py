import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

class Loginpage:

    def __init__(self,driver):
        self.driver = driver
        self.login_button =(By.ID,'login-btn')
        self.username = (By.ID,'email')
        self.password = (By.ID,'password')
        self.submit_btn = (By.XPATH,'//a[@class="btn login-btn"]')

    def openurl(self):
        self.driver.get('https://www.guvi.in/')
        self.driver.maximize_window()

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_pswrd(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.submit_btn).click()


