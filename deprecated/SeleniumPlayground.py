import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urllib.parse import urlparse

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def AmazonLogin(driver, email):
    emailInput = driver.find_element(By.CSS_SELECTOR, "input[id='ap_email']")
    emailInput.send_keys(email)

    continueButton = driver.find_element(By.CSS_SELECTOR, "input[id='continue']")
    continueButton.click()

def AmazonFindItemAddToCart(driver, product):
    searchTextBox = driver.find_element(By.CSS_SELECTOR, "input[id='twotabsearchtextbox']")
    searchTextBox.send_keys(product)

    searchSubmitButton = driver.find_element(By.CSS_SELECTOR, "input[id='nav-search-submit-button']")
    searchSubmitButton.click()

    # "first" result sometimes isn't showing up in the actual page, making this test flaky ?
    wait = WebDriverWait(driver, 5)
    productItem = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "[data-cel-widget^='search_result_'] [data-component-type='s-product-image'] > a")))
    productItem.click()
    
    addCart = driver.find_element(By.CSS_SELECTOR, "input[value='Add to Cart']")
    addCart.click()

def test_GoogleNavigateToHome(driver):
    expectedUrl = "https://www.google.com/"
    
    driver.get(expectedUrl)

    actualUri = urlparse(driver.current_url)
    expectedUri = urlparse(expectedUrl)

    # Deletes fragments
    actual = actualUri._replace(fragment="").geturl()
    expected = expectedUri._replace(fragment="").geturl()

    assert actual == expected
@pytest.mark.parametrize("product,email",[
    ("Crysis Remastered Trilogy", "w4riu3gyyfid20at@gmail.com")
])
def test_AmazonLoginAfterBuyNow(driver, product, email):
    driver.get("https://www.amazon.com/")

    AmazonFindItemAddToCart(driver, product)
    buyNowButton = driver.find_element(By.CSS_SELECTOR, "input[data-feature-id='proceed-to-checkout-action']")
    buyNowButton.click()

    AmazonLogin(driver, email)
    errMessageBox = driver.find_element(By.CSS_SELECTOR, "[id='auth-error-message-box']")
    assert errMessageBox is not None
    errMessage = errMessageBox.find_element(By.CSS_SELECTOR, "span")
    assert errMessage.text == "We cannot find an account with that email address"

@pytest.mark.parametrize("email",[
    ("w4riu3gyyfid20at@gmail.com")
])
def test_AmazonLoginFromHome(driver, email):
    driver.get("https://www.amazon.com/")

    accountLoginButton = driver.find_element(By.CSS_SELECTOR, "a[data-nav-role='signin']")
    accountLoginButton.click()

    AmazonLogin(driver, email)
    errMessageBox = driver.find_element(By.CSS_SELECTOR, "[id='auth-error-message-box']")
    assert errMessageBox is not None
    errMessage = errMessageBox.find_element(By.CSS_SELECTOR, "span")
    assert errMessage.text == "We cannot find an account with that email address"

@pytest.mark.parametrize("productList",[
    (["Crysis Remastered Trilogy"]),
    (["Crysis Remastered Trilogy", "StarCraft books"]),
    (["Crysis Remastered Trilogy", "StarCraft books", "Halo Infinite"])
])
def test_AmazonAddCart(driver, productList):
    # Flaky if prompted for human verification code
    driver.get("https://www.amazon.com/")
    
    for product in productList:
        AmazonFindItemAddToCart(driver, product)

    cartButton = driver.find_element(By.XPATH, "//*[@id=\"sw-gtc\"]/span/a")
    cartButton.click()
    
    productListElement = driver.find_element(By.CSS_SELECTOR, "[data-name='Active Items']")
    productElements = productListElement.find_elements(By.CSS_SELECTOR, "[data-subtotal]")
    actual = len(productElements)
    expected = len(productList)

    assert actual == expected