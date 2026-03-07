#pytest is testing framework for python used to integration
#regression and end to end test
import time
import unittest
from unittest import TestCase
from selwithvirtualenv_setup import Browser

# if __name__ == "__main__":
#     url="https://www.guvi.in/"
#     my_browser = Browser(url)
#     my_browser.launch_application()
#     title_of_the_page = my_browser.get_title()
#     if title_of_the_page == "HCL GUVI | Learn to code in your native language":
#             print("Passed")
#     else:
#         print("Failed")
#     url_of_page = my_browser.url
#     if url_of_page  == url:
#         print("Passed")
#     else:
#         print("Failed")
#     time.sleep(2)
#     my_browser.close_browser()

url ="https://www.guvi.in/"
browser = Browser('url')
my_browser = Browser(url)

class TestBrowser(TestCase):

    def testcase_title_validation_positive(self):
        title_of_the_page = my_browser.get_title()
        my_browser.launch_application()
        if title_of_the_page == "HCL GUVI | Learn to code in your native language":
            print("Passed")
        else:
            print("Failed")

    def testcase_title_validation_negative(self):
        title_of_the_page = my_browser.get_title()
        if title_of_the_page != "HCL GUVI | Learn to code ":
            print("Passed")
        else:
             print("Failed")
        time.sleep(2)
        my_browser.close_browser()



# postive --> right steps should leads to actual/excepted behaviour
# negative --> wrong steps leads to errors
