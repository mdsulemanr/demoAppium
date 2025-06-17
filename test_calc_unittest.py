# unittest Syntax to support htmltestrunner for report generation

import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "2a38caeb01047ece"
        options.automation_name = "UiAutomator2"
        options.platform_version = "10"
        options.app_package = "com.dencreak.dlcalculator"
        options.app_activity = "com.dencreak.dlcalculator.DLCalculatorActivity"
        options.no_reset = False
        options.full_reset = False

        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        self.wait = WebDriverWait(self.driver, 15)

    def test_addition(self):
        # 2 + 3 = 5
        self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_btn_d_b"))).click()
        self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_img_d_d"))).click()
        self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_btn_d_c"))).click()
        self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_img_e_d"))).click()

        # Get result and assert
        result_elem = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.dencreak.dlcalculator:id/lay_normal_body_val")))
        result_text = result_elem.text.strip()
        self.assertEqual(result_text, "5", f"Expected result to be 5 but got {result_text}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
