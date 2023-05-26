from .base_page import BasePage
from .locators import ProductPageLocators as Locators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_review_button()
        self.should_be_add_to_basket_button()
        self.should_be_wishlist_button()

    def should_be_review_button(self):
        assert self.is_element_present(*Locators.REVIEW_BUTTON), 'No "Review" button!'

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*Locators.ADD_TO_BASKET_BUTTON), 'No "Add to basket" button!'

    def should_be_wishlist_button(self):
        assert self.is_element_present(*Locators.WISHLIST_BUTTON), 'No "Add to wishlist" button!'

    def should_be_correct_item_name(self, item_name_heading):
        item_name_alert = self.browser.find_element(*Locators.ITEM_NAME_ALERT).text
        assert item_name_heading == item_name_alert, 'Item name in heading and in alert differ!'
    
    def should_be_correct_item_price(self, item_price):
        basket_checkout_sum = self.browser.find_element(*Locators.BASKET_CHECKOUT_ALERT).text
        assert item_price == basket_checkout_sum, 'Basket checkout sum and item sum differ!'

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*Locators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        # self.solve_quiz_and_get_code()

    def success_message_should_be_missing(self):
        assert self.is_element_missing(*Locators.SUCCESS_MESSAGE)

    def success_message_should_disappear(self):
        assert self.has_element_disappeared(*Locators.SUCCESS_MESSAGE)

