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

        # Find anchor element to corresponding product image
        product = self.driver.find_element("css selector",f"[href^='../products/']:has(> [alt*='{productName}'])")

        # Store anchor href in product URL for ProductPage instantiation
        productUrl = product.get_attribute("href")
        
        product.click()
        return ProductPage(self.driver, productUrl)