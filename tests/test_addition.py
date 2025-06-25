from pages.addition_page import AdditionPage
from constants.assertions import ADDITION_RESULT


def test_addition(driver):
    add_page = AdditionPage(driver)
    add_page.perform_addition()
    result = add_page.get_result_text()
    assert result == ADDITION_RESULT, f"Expected {ADDITION_RESULT}, got {result}"
