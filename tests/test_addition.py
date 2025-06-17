# tests/test_addition.py

from pages.calculator_page import CalculatorPage


class TestCalculator:

    def test_addition_of_2_and_3(self, driver):
        calc_page = CalculatorPage(driver)
        calc_page.perform_addition_of_2_and_3()
        result = calc_page.get_result_text()
        assert result == "5", f"Expected result to be 5 but got {result}"
