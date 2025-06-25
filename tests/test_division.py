from pages.division_page import DivisionPage
from constants.assertions import DIVISION_RESULT


def test_division(driver):
    div_page = DivisionPage(driver)
    div_page.perform_division()
    result = div_page.get_result_text()
    assert result == DIVISION_RESULT, f"Expected {DIVISION_RESULT}, got {result}"
