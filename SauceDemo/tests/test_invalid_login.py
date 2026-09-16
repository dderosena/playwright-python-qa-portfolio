from playwright.sync_api import expect

def test_invalid_login(page):
    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "wrong_user")
    page.fill("#password", "wrong_password")

    page.click("#login-button")

    expect(
        page.locator("[data-test='error']")
    ).to_be_visible()