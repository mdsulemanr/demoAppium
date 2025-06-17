# Converted unittest to Pytest Syntax to support Allure for report generation

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


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


def test_addition(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_btn_d_b"))).click()
    wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_img_d_d"))).click()
    wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_btn_d_c"))).click()
    wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_img_e_d"))).click()

    result_elem = wait.until(EC.presence_of_element_located(
        (AppiumBy.ID, "com.dencreak.dlcalculator:id/lay_normal_body_val")))
    result_text = result_elem.text.strip()
    assert result_text == "5", f"Expected result to be 5 but got {result_text}"
