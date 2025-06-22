from appium.webdriver.common.appiumby import AppiumBy
from base.base_page import BasePage
from utils.logger import get_logger


class CalculatorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)

    # Locators
    _btn_2 = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_btn_d_b")
    _btn_3 = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_btn_d_c")
    _btn_plus = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_img_d_d")
    _btn_multiply = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_img_b_d")
    _btn_divide = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_img_a_d")
    _btn_equals = (AppiumBy.ID, "com.dencreak.dlcalculator:id/pad_img_e_d")
    _result = (AppiumBy.ID, "com.dencreak.dlcalculator:id/lay_normal_body_val")

    # Actions
    def perform_addition(self):
        self.logger.info("Performing addition 2 + 3")
        self.wait_and_click(self._btn_2)
        self.wait_and_click(self._btn_plus)
        self.wait_and_click(self._btn_3)
        self.wait_and_click(self._btn_equals)

    def perform_multiplication(self):
        self.logger.info("Performing multiplication 2 × 3")
        self.wait_and_click(self._btn_2)
        self.wait_and_click(self._btn_multiply)
        self.wait_and_click(self._btn_3)
        self.wait_and_click(self._btn_equals)

    def perform_division(self):
        self.logger.info("Performing division 3 ÷ 2")
        self.wait_and_click(self._btn_3)
        self.wait_and_click(self._btn_divide)
        self.wait_and_click(self._btn_2)
        self.wait_and_click(self._btn_equals)

    def get_result_text(self):
        result = self.get_text(self._result)
        self.logger.info(f"Result obtained: {result}")
        return result
