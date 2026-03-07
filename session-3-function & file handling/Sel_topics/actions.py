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
driver.get('https://automationtesting.co.uk/actions.html')
driver.maximize_window()
time.sleep(2)

action = ActionChains(driver)
source = driver.find_element(By.ID,"dragtarget")
target = driver.find_element(By.XPATH,'(//div[@class="droptarget"])[2]')
action.drag_and_drop(source=source,target=target).perform()
time.sleep(2)

#double click element
dou_cl_ele = driver.find_element(By.ID,"doubClickStartText")
action.double_click(dou_cl_ele).perform()
time.sleep(2)

#holding element
hold_ele  = driver.find_element(By.XPATH,'//p[@class="action_start_text"]')
action.click_and_hold(hold_ele).perform()
# action.release(hold_ele).perform()
time.sleep(2)

#hold,shift element
hold_sif_ele = driver.find_element(By.XPATH,'//p[text()="Hold Shift & Click Here"]')
action.key_down(Keys.SHIFT)
action.click_and_hold(hold_sif_ele).perform()
time.sleep(2)