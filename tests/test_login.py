import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("driver_init")
class TestLogin:
    @pytest.mark.reg
    @pytest.mark.parametrize("email,password",[
        ("stevencaior.dummy@gmail.com", "Password123_"),
    ])
    def test_NoAccount(self, email, password):
        home_page = HomePage(self.driver)

        login_page = home_page.navigate_login()
        login_page.login(email, password)

        errMsg = "Looks like you don't have a ResiSTORE Account."
        assert login_page.alert_danger.text[:len(errMsg)] == errMsg