from .base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver, productUrl):
        super().__init__(driver)
        self.url = productUrl

    @property
    def element_productName(self):
        return self.driver.find_element("css selector", "h2")