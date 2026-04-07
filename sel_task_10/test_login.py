import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


class Testlogin:

    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_positive_login(self,setup):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.XPATH, '//input[@class="submit-button btn_action"]').click()
        time.sleep(2)

    def test_negative_login(self,setup):
        self.driver.find_element(By.ID, 'user-name').send_keys('incorrect')
        self.driver.find_element(By.ID, 'password').send_keys('no_secret_sauce')
        self.driver.find_element(By.XPATH, '//input[@class="submit-button btn_action"]').click()
        time.sleep(2)
