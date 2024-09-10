from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://resi.store/"

    @property
    def image_resistore(self):
        return self.driver.find_element("css selector", "[alt='ResiStore!']")
    
    @property
    def status(self):
        return self.driver.find_element("css selector", ".avalibility-banner1 h3")
    
    def select_product(self, productName):
        from .product_page import ProductPage

        product = self.driver.find_element("css selector",f"[href^='../products/']:has(> [alt*='{productName}'])")
        productUrl = product.get_attribute("href")
        product.click()
        return ProductPage(self.driver, productUrl)