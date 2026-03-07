import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://automationtesting.co.uk/loader.html')
driver.maximize_window()
time.sleep(2)
wait = WebDriverWait(driver,10)
print(wait.until(expected_conditions.visibility_of_element_located((By.ID,"loaderBtn"))).text)
