from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators as Locators
from .pages.basket_page import BasketPage
import pytest

link_parameters = []
for x in range(0, 10):
    if x != 7:
        link_parameters.append(f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{x}')
    else:
        link_parameters.append(pytest.param(f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{x}', marks=pytest.mark.xfail))

@pytest.mark.skip
@pytest.mark.parametrize('link', link_parameters)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_basket()
    item_name_heading = browser.find_element(*Locators.ITEM_NAME_HEADING).text
    item_price = browser.find_element(*Locators.ITEM_PRICE).text
    product_page.should_be_correct_item_price(item_price)
    product_page.should_be_correct_item_name(item_name_heading)

@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link, 4)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_basket()
    product_page.success_message_should_be_missing()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link, 4)
    product_page.open()
    product_page.should_be_product_page()
    product_page.success_message_should_be_missing()

@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link, 4)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_basket()
    product_page.success_message_should_disappear()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_view_basket_button()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message()
    basket_page.basket_items_should_be_missing()