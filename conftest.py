# conftest.py

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.config import CONFIG


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = CONFIG["platformName"]
    options.device_name = CONFIG["deviceName"]
    options.automation_name = CONFIG["automationName"]
    options.platform_version = CONFIG["platformVersion"]
    options.app_package = CONFIG["appPackage"]
    options.app_activity = CONFIG["appActivity"]
    options.no_reset = CONFIG["noReset"]

    driver = webdriver.Remote(CONFIG["appiumServerURL"], options=options)
    yield driver
    driver.quit()
