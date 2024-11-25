import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'  # 'normal', 'none'

    browser.config.driver = webdriver.Chrome(options=options)
    browser.config.base_url = 'https://www.w3schools.com'

    yield

    browser.quit()
