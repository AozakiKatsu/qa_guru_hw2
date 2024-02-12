from selene import browser
import pytest
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

@pytest.fixture(scope='function')
def browser_size():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
