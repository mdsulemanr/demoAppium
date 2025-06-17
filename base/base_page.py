# base/base_page.py - Base Page (Common Utilities)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_and_click(self, locator):
        self.wait.until(EC.presence_of_element_located(locator)).click()

    def get_text(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text.strip()
