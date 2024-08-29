# Template for common elements in all pages, including the homepage

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(self.url)

    @property
    def nav_login(self):
        return self.driver.find_element("css selector", f"[href='login/']")

    def navigate(self, tab):
        self.open()
        tabLink = self.driver.find_element("css selector", f"[href='{tab}/']")
        tabLink.click()
    
    def navigate_login(self):
        from .login_page import LoginPage

        self.open()
        self.nav_login.click()
        return LoginPage(self.driver)
    
    def search(self, query):
        from selenium.webdriver.common.keys import Keys

        searchBar = self.driver.find_element("css selector", "[aria-label='Search']")
        searchBar.send_keys(query)
        searchBar.send_keys(Keys.RETURN)