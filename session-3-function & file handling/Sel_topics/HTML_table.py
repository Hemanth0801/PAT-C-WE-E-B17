import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument('--incognito')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
driver.get('https://automationtesting.co.uk/tables.html')
driver.maximize_window()
time.sleep(2)

table_doc = driver.find_elements(By.XPATH,'//table[@class="sortable"]/tbody/tr[1]/td')
for table_doc_but in table_doc:
    print(table_doc_but.text)




