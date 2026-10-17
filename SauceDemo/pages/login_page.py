class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/")


    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)

        login_button = self.page.locator("#login-button")

        print("Login buttons found:", login_button.count())
        print("Button visible:", login_button.is_visible())
        print("Button enabled:", login_button.is_enabled())

        login_button.click()