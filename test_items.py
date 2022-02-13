from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_is_present(browser):
    browser.get(link)
    time.sleep(5)
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-cart")
    # add_to_cart_button = WebDriverWait(browser, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-cart")))
    assert add_to_cart_button is not None, "There is no <Add to Cart> button on the page!"

