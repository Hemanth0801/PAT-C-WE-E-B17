import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://automationtesting.co.uk/browserTabs.html')
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@type="submit"]').click()
time.sleep(2)

#getting id from parent window and storing inside parent_window varable
parent_window = driver.current_window_handle

#getting id of all opened window handles and storing inside tabs variables
tabs = driver.window_handles
print(len(tabs))
print(driver.title)
print(tabs)
for each_tab in tabs:
    driver.switch_to.window(each_tab)
    print(driver.title)
    print(driver.current_url)
    time.sleep(2)
driver.switch_to.window(parent_window)
time.sleep(2)



