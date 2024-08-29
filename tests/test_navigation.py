import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage

@pytest.mark.usefixtures("driver_init")
class TestNavigation:
    @pytest.mark.smoke
    @pytest.mark.parametrize("tab",[
        ("products"),
        ("downloads"),
        ("hours"),
        ("getinvolved"),
    ])
    def test_BasicNavigation(self, tab):
        home_page = HomePage(self.driver)
        home_page.navigate(tab)

        assert self.driver.current_url == f"https://resi.store/{tab}/"

    @pytest.mark.reg
    @pytest.mark.parametrize("productName",[
        ("10k Ohm Resistor"),
        ("220 Ohm Resistor"),
        ("100k Ohm Resistor"),
        ("1k Ohm Resistor"),
    ])
    def test_NavigateToProduct(self, productName):
        products_page = ProductsPage(self.driver)
        products_page.open()
        product_page = products_page.select_product(productName)
        
        assert product_page.element_productName.text[:len(productName)] == productName