from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class DynamicXpath:

    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('https://www.guvi.in/')
        time.sleep(3)

    def test_dynamic_xpath(self):
        live_classes = self.driver.find_element(By.XPATH,"//a[contains(text(),'LIVE Classes')]")

        parent_element = live_classes.find_element(By.XPATH,'./parent::*')

        first_child = parent_element.find_element(By.XPATH,'./child::*[1]')
        print("First Child Tag Name:", first_child.tag_name)

        second_sibling = live_classes.find_element(By.XPATH,"./following-sibling::*[2]")
        print("second sibling: ", second_sibling.text)

        href_parent = self.driver.find_element(By.XPATH, "//a[@href='/courses/']/parent::*")
        print("parent using href located")


        ancestors = self.driver.find_elements(By.XPATH,"//a[contains(text(),'Practice')]/ancestor::*")
        print("Total Ancestors:", len(ancestors))

        following_siblings = self.driver.find_elements(By.XPATH,"//a[contains(text(),'Practice')]/following-sibling::*")
        print("Following Siblings:", len(following_siblings))

        preceding_elements = self.driver.find_elements(By.XPATH,"//a[contains(text(),'Practice')]/preceding::*")
        print("Preceding Elements:", len(preceding_elements))

        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()