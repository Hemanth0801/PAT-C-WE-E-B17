import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com/droppable/")
    yield driver
    driver.quit()


def test_drag_and_drop_positive(driver):
    iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
    driver.switch_to.frame(iframe)

    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    assert target.text == "Dropped!"
    driver.switch_to.default_content()


def test_drag_and_drop_negative(driver):
    driver.refresh()
    iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
    driver.switch_to.frame(iframe)

    target = driver.find_element(By.ID, "droppable")

    assert target.text != "Dropped!"
    driver.switch_to.default_content()