# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# driver.get("https://www.guvi.in/")
# print(driver.title)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Testurl():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def __init__(self,url):
        self.url = url

    def invoke_browser_url(self):
        self.driver.get(self.url)

    def validate_url(self):
        if self.url == self.driver.current_url:
            return f"TestCase Passed, current url is {self.url}"
        else:
            return f"TestCase Failed, current url is {self.url}"

    def close_browser(self):
        self.driver.quit()

if __name__ == '__main__':
    test_browser = Testurl('https://www.guvi.in/')
    test_browser.invoke_browser_url()
    print(test_browser.validate_url())
    test_browser.close_browser()

# Task: Create a method to validate title of the page and print the result as pass/ fail