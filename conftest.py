import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "2a38caeb01047ece"
    options.automation_name = "UiAutomator2"
    options.platform_version = "10"
    options.app_package = "com.dencreak.dlcalculator"
    options.app_activity = "com.dencreak.dlcalculator.DLCalculatorActivity"
    options.no_reset = False

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()
