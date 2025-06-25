from appium.webdriver.common.appiumby import AppiumBy
from base.base_page import BasePage


class DivisionPage(BasePage):
    _btn_6 = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_btn_c_c")
    _btn_3 = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_btn_d_c")
    _btn_divide = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_img_a_d")
    _btn_equals = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_img_e_d")
    _result = (AppiumBy.ID, "com.dencreak.dlcalculator:id/lay_normal_body_val")

    def perform_division(self):
        self.wait_and_click(self._btn_6)
        self.wait_and_click(self._btn_divide)
        self.wait_and_click(self._btn_3)
        self.wait_and_click(self._btn_equals)

    def get_result_text(self):
        return self.get_text(self._result)
