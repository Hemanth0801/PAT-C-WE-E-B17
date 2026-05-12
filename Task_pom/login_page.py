from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_xpath = "//input[@name='username']"
        self.password_xpath = "//input[@name='password']"
        self.login_btn_xpath = "//button[@type='submit']"
        self.profile_xpath = "//span[@class='oxd-userdropdown-tab']"
        self.logout_xpath = "//a[text()='Logout']"

    def open_website(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def enter_username(self, username):
        wait = WebDriverWait(self.driver, 20)
        username_box = wait.until(EC.visibility_of_element_located((By.XPATH, self.username_xpath)))
        username_box.clear()
        username_box.send_keys(username)

    def enter_password(self, password):
        password_box = self.driver.find_element(By.XPATH,self.password_xpath)
        password_box.clear()
        password_box.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_btn_xpath).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        time.sleep(3)

    def logout(self):

        wait = WebDriverWait(self.driver, 20)
        profile = wait.until(EC.element_to_be_clickable((By.XPATH, self.profile_xpath)))
        profile.click()
        logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, self.logout_xpath)))
        logout_btn.click()

    def is_login_button_displayed(self):

        try:
            wait = WebDriverWait(self.driver, 20)
            login_btn = wait.until(EC.visibility_of_element_located((By.XPATH, self.login_btn_xpath)))
            return login_btn.is_displayed()
        except NoSuchElementException:
            return False