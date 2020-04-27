import time
from selenium.common.exceptions import NoSuchElementException
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    button = None
    try:
        browser.find_element_by_css_selector('button.btn-add-to-basket')
    except NoSuchElementException:
        button = False
    else:
        button = True
    
    assert button == True, "Add to basket button is absent"