import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from .locators import BasePageLocators

class BasePage:
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, search_method, locator):
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((search_method, locator)))
        except (TimeoutException):
            return False
        return True

    def is_element_missing(self, search_method, locator):
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((search_method, locator)))
        except (TimeoutException):
            return True
        return False
    
    def has_element_disappeared(self, search_method, locator):
        try:
            WebDriverWait(self.browser, self.timeout).until_not(EC.presence_of_element_located((search_method, locator)))
        except (TimeoutException):
            return False
        return True
    
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Unable to find login link'

    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        login_link.click()

    def should_be_view_basket_button(self):
        assert self.is_element_present(*BasePageLocators.VIEW_BASKET_BUTTON), 'Unable to find "View basket" button'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
