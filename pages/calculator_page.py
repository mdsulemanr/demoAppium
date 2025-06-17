# pages/calculator_page.py

from appium.webdriver.common.appiumby import AppiumBy
from base.base_page import BasePage


class CalculatorPage(BasePage):
    # Locators (centralized)
    _btn_2 = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_btn_d_b")
    _btn_plus = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_img_d_d")
    _btn_3 = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_btn_d_c")
    _btn_equals = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_img_e_d")
    _result = (AppiumBy.ID, "com.dencreak.dlcalculator:id/lay_normal_body_val")

    # High-level Actions (Page behaviors)
    def perform_addition_of_2_and_3(self):
        self.wait_and_click(self._btn_2)
        self.wait_and_click(self._btn_plus)
        self.wait_and_click(self._btn_3)
        self.wait_and_click(self._btn_equals)

    def get_result_text(self):
        return self.get_text(self._result)
