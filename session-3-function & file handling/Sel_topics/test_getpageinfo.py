from selwithvirtualenv_setup import Browser

def test_getbrowserpageinfo():
    url = 'https://www.saucedemo.com/'
    browser = Browser(url)
    browser.launch_application()
    print(browser.get_title())
    browser.login_()
    browser.close_browser()
