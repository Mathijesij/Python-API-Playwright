import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com")
    yield driver
    driver.close()