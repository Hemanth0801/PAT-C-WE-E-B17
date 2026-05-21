import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser_setup():

    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.zenclass.in/login")

    yield page

    browser.close()

    playwright.stop()