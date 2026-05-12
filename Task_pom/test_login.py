from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_successful_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login = LoginPage(driver)
    login.open_website()
    login.login("Admin", "admin123")
    assert "dashboard" in driver.current_url.lower()
    login.logout()
    driver.quit()


def test_unsuccessful_login():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login = LoginPage(driver)
    login.open_website()
    login.login("Admin", "wrongpassword")
    time.sleep(2)
    assert "auth/login" in driver.current_url
    driver.quit()


def test_username_input_box():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login = LoginPage(driver)
    login.open_website()
    wait = WebDriverWait(driver, 20)
    username_box = wait.until(EC.visibility_of_element_located(("xpath", "//input[@name='username']")))
    assert username_box.is_displayed()
    driver.quit()


def test_password_input_box():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login = LoginPage(driver)
    login.open_website()
    wait = WebDriverWait(driver, 20)
    password_box = wait.until(EC.visibility_of_element_located(("xpath", "//input[@name='password']")))
    assert password_box.is_displayed()
    driver.quit()


def test_login_button():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login = LoginPage(driver)
    login.open_website()
    assert login.is_login_button_displayed()
    driver.quit()


def test_logout_functionality():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login = LoginPage(driver)
    login.open_website()
    login.login("Admin", "admin123")
    login.logout()
    assert "login" in driver.current_url.lower()
    driver.quit()