from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://resi.store/login/"

    @property
    def alert_danger(self):
        return self.driver.find_element("css selector", ".alert-danger")

    def login(self, email, password):
        emailInput = self.driver.find_element("name", "email")
        emailInput.send_keys(email)

        passwordInput = self.driver.find_element("name", "password")
        passwordInput.send_keys(password)
        
        submitInput = self.driver.find_element("name", "submit-std")
        submitInput.click()