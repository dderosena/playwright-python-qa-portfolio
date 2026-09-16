import pytest
from playwright.sync_api import expect

@pytest.fixture
def logged_in_page(page):
    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    return page
