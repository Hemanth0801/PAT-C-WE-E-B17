#pytest is testing framework for python used to integration
#regression and end to end test

#steps
#install pytest
# import pytest in the .py files

#rules
#pytest files are discovered based on dfile name extension, meaning file should start with test or end with test
#class name should start with test
#function name should have test starting of the name

# def test_dummy():                                                #pytest  #pytest -v -s
#     print("Hello World")
# def test_dummy1(): print("Hello World")
# def dummy2(): print("Hello World")



from selwithvirtualenv_setup import Browser


url = 'https://www.guvi.in/'
browser = Browser('url')
my_browser = Browser(url)

def launch_get_tittle():
    title_of_the_page = my_browser.get_title()
    if title_of_the_page == "HCL GUVI | Learn to code in your native language":
        print("Passed")
    else:
        print("Failed")


