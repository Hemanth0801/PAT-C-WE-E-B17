import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from task_headless_browser.loginpage import Loginpage


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(setup):
    driver = setup
    page =Loginpage(driver)
    page.openurl()
    time.sleep(5)
    page.click_login()
    time.sleep(2)
    assert "sign-in" in driver.current_url

    page.enter_username("nasinahemanth0801@gmail.com")
    page.enter_pswrd("Hemu@0801")
    page.click_submit()
    time.sleep(2)
    assert "dashboard" in driver.current_url or "GUVI" in driver.title

def test_invalid_login(setup):
    driver = setup
    page = Loginpage(driver)
    page.openurl()
    time.sleep(5)
    page.click_login()
    time.sleep(10)

    page.enter_username("nnhhaa@gmail.com")
    page.enter_pswrd("12345")
    page.click_submit()
    time.sleep(2)

    assert "sign-in" in driver.current_url or "login" in driver.page_source.lower()

def test_input_fields_visible(setup):
    driver =setup
    page = Loginpage(driver)

    page.openurl()
    page.click_login()
    time.sleep(5)

    assert driver.find_element(*page.username).is_displayed()
    assert driver.find_element(*page.password).is_displayed()

def test_submit_button(setup):
    driver = setup
    page = Loginpage(driver)

    page.openurl()
    page.click_login()
    time.sleep(2)

    btn = driver.find_element(*page.submit_btn)
    assert btn.is_enabled()
