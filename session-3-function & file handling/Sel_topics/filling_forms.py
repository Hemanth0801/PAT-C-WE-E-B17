import time
from logging import raiseExceptions
from operator import truediv
from sys import exception

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(10)
driver.find_element(By.ID,"firstName").send_keys("Demo")
driver.find_element(By.ID,"lastName").send_keys("Auto")
driver.find_element(By.ID,"userEmail").send_keys("A123@gmail.com")
driver.find_element(By.ID, "userNumber").send_keys("1234567890")
driver.find_element(By.ID,"subjectsInput").send_keys("Python")
driver.find_element(By.ID,"currentAddress").send_keys("chennai")
time.sleep(3)
driver.save_screenshot("filling_forms.png")
driver.quit()