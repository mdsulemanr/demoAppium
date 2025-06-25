from pages.multiplication_page import MultiplicationPage
from constants.assertions import MULTIPLICATION_RESULT


def test_multiplication(driver):
    mult_page = MultiplicationPage(driver)
    mult_page.perform_multiplication()
    result = mult_page.get_result_text()
    assert result == MULTIPLICATION_RESULT, f"Expected {MULTIPLICATION_RESULT}, got {result}"
