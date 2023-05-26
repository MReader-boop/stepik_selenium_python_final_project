from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_INVALID = (By.CSS_SELECTOR, '#login_link_invalid')
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, 'header a.btn-default')

class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    REVIEW_BUTTON = (By.ID, 'write_review')
    WISHLIST_BUTTON = (By.CLASS_NAME, 'btn-wishlist')
    ITEM_NAME_HEADING = (By.TAG_NAME, 'h1')
    ITEM_NAME_ALERT = (By.CSS_SELECTOR, '.alertinner > strong')
    BASKET_CHECKOUT_ALERT = (By.CSS_SELECTOR, '.alertinner p strong')
    ITEM_PRICE = (By.CSS_SELECTOR, '.product_main p')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-success')

class BasketPageLocators:
    # Селектор для сообщения о пустой корзине внизу страницы. Не самый элегантный, "спасибо" отсутствию семантики.
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
    FIRST_BASKET_ITEM = (By.ID, 'basket_formset')