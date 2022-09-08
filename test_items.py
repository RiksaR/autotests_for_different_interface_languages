import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    elements = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(elements) > 0, 'The "Add to cart" button must be present'
