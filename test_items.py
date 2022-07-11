import time
import pytest
from selenium.webdriver.common.by import By


def test_page_has_the_add_to_basket_button(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    # open the page
    browser.get(link)

    # set the timeout
    time.sleep(30)

    # check the page has the add to basket button
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket"), "The button is absent on the page"






