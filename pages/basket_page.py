from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)

    def basket_items_should_be_missing(self):
        assert self.is_element_missing(*BasketPageLocators.FIRST_BASKET_ITEM)