from playwright.sync_api import expect
from SauceDemo.pages.login_page import LoginPage

def test_invalid_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("invalid_user", "wrong_password")

    expect(
        page.locator("[data-test='error']")
    ).to_contain_text(
        "Username and password do not match"
    )