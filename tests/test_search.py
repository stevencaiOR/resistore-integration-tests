import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("driver_init")
class TestSearch:
    @pytest.mark.smoke
    @pytest.mark.parametrize("query",[
        ("resistor"),
        ("capacitor")
    ])
    def test_BasicSearch(self, query):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.search(query)

        header = self.driver.find_element("css selector", "h1")
        assert header.text == f"Results for '{query}'"