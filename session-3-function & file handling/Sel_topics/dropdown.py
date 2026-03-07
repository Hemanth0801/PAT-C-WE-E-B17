import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://automationtesting.co.uk/dropdown.html')
driver.maximize_window()
time.sleep(2)

#using tag for dropdown menus
select = Select(driver.find_element(By.TAG_NAME,'select'))
select.select_by_index(2)
time.sleep(2)
# select.select_by_value('Mercedes')

#handling radio buttons with dynamic approach
radio_buttons = driver.find_elements(By.XPATH,"//label[contains(@for, 'demo-priority-')]")
for each_radio_btns in radio_buttons:
    each_radio_btns.click()
    time.sleep(2)


#clicking on all checkboxes
check_box = driver.find_elements(By.XPATH, '//label[contains(@for, "cb_")]')
for check_button in check_box:
    if check_button.is_selected():
        continue
    else:
        check_button.click()
        time.sleep(2)

#html tables



