import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.guvi.in/")
driver.maximize_window()
time.sleep(1)
driver.refresh()
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.save_screenshot("guvi.png")
driver.close()


