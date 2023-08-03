import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def init_browser():
    browser.driver.set_window_size(1920, 1080)
