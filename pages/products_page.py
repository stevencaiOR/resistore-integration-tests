from .base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://resi.store/products/"

    @property
    def element_productName(self):
        return self.driver.find_element("css selector", "h2")
    
    def select_product(self, productName):
        from .product_page import ProductPage

        product = self.driver.find_element("css selector",f"[href^='../products/']:has(> [alt*='{productName}'])")
        productUrl = product.get_attribute("href")
        product.click()
        return ProductPage(self.driver, productUrl)