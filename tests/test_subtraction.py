from pages.subtraction_page import SubtractionPage
from constants.assertions import SUBTRACTION_RESULT


def test_subtraction(driver):
    sub_page = SubtractionPage(driver)
    sub_page.perform_subtraction()
    result = sub_page.get_result_text()
    assert result == SUBTRACTION_RESULT, f"Expected {SUBTRACTION_RESULT}, got {result}"
