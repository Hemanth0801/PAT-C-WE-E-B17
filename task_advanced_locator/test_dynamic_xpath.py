import pytest
from dynamic_xpath import DynamicXpath

@pytest.fixture
def obj():
    driver = DynamicXpath()
    driver.setup()
    yield driver
    driver.teardown_method()


def test_xpath(obj):
    obj.test_dynamic_xpath()