from playwright.sync_api import expect

def test_locked_user(page):
    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "locked_out_user")
    page.fill("#password","secret_sauce")
    page.click("#login-button")

    expect(
        page.locator("[data-test='error']")
    ).to_contain_text("locked out")