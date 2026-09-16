from playwright.sync_api import expect


def test_logout(logged_in_page):
    page = logged_in_page

    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator("#login-button")).to_be_visible()
