from playwright.sync_api import expect

def test_inventory(logged_in_page):
    page = logged_in_page

    products = page.locator(".inventory_item")
    
    expect(products).to_have_count(6)

    expect(page.locator(".inventory_item_name")).to_have_count(6)
    expect(page.locator(".inventory_item_price")).to_have_count(6)
    expect(page.locator(".inventory_item img")).to_have_count(6)
    expect(page.locator("button[data-test^='add-to-cart']")).to_have_count(6)