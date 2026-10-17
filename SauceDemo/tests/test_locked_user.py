from SauceDemo.pages.login_page import LoginPage
from playwright.sync_api import expect

def test_locked_user(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    expect(
        page.locator("[data-test='error']")
    ).to_contain_text("locked out")