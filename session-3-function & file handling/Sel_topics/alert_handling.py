import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.selenium.dev/selenium/web/alerts.html#')
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,'prompt').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element(By.ID,'prompt').click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.find_element(By.ID,'prompt').click()
time.sleep(2)
driver.switch_to.alert.send_keys('test')
time.sleep(2)
driver.switch_to.alert.accept()




