import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("driver_init")
class TestHome:
    def test_HomeVisibility(self):
        home_page = HomePage(self.driver)
        home_page.open()

        statusPrefix = "The physical store is currently "
        assert home_page.image_resistore is not None
        assert home_page.status.text[:len(statusPrefix)] == statusPrefix