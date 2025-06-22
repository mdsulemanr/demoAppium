import allure
from base.base_test import BaseTest
from pages.calculator_page import CalculatorPage


@allure.feature("Calculator Operations")
class TestCalculator(BaseTest):

    def test_addition(self, driver):
        self.calc_page = CalculatorPage(driver)
        self.calc_page.perform_addition()
        assert self.calc_page.get_result_text() == "5"

    def test_multiplication(self, driver):
        self.calc_page = CalculatorPage(driver)
        self.calc_page.perform_multiplication()
        assert self.calc_page.get_result_text() == "6"

    def test_division(self, driver):
        self.calc_page = CalculatorPage(driver)
        self.calc_page.perform_division()
        assert self.calc_page.get_result_text() in ["1.5", "1.50"]  # Some calculators round differently
