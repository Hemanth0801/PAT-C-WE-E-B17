import time
from argparse import Action
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://automationtesting.co.uk/buttons.html')
driver.maximize_window()
time.sleep(2)

actions = ActionChains(driver)
move_to_bttn = driver.find_element(By.ID,'btn_three')
actions.move_to_element(move_to_bttn).click().perform()#when we use action we need to ise perform at the end
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

print(driver.find_element(By.ID,'btn_four').is_enabled())

