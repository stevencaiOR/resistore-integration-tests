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

    @pytest.mark.smoke
    @pytest.mark.parametrize("productName",[
        ("10k Ohm Resistor"),
        ("220 Ohm Resistor"),
        ("100k Ohm Resistor"),
        ("1k Ohm Resistor"),
    ])
    def test_NavigateToProduct(self, productName):
        # Create instance of products page, then navigate
        products_page = ProductsPage(self.driver)
        products_page.open()

        # Navigate to specified product page
        product_page = products_page.select_product(productName)
        
        # Assert element containing product name on product page matches initial query
        assert product_page.element_productName.text[:len(productName)] == productName