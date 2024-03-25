import pytest
from selenium.webdriver.common.by import By
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_add_to_basket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    basket_input = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert basket_input, "Button not found"
    basket_input[0].click()

    time.sleep(5)





