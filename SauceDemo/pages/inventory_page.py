class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_backpack_to_cart(self):
        self.page.click("#add-to-cart-sauce-labs-backpack")

    def add_bike_light_to_cart(self):
        self.page.click("#add-to-cart-sauce-labs-bike-light")

    def add_bolt_tshirt_to_cart(self):
        self.page.click("#add-to-cart-sauce-labs-bolt-t-shirt")

    def remove_backpack(self):
        self.page.click("#remove-sauce-labs-backpack")

    def sort_low_to_high(self):
        self.page.select_option(".product_sort_container", value="lohi")

    def sort_high_to_low(self):
        self.page.select_option(".product_sort_container", value="hilo")

    def logout(self):
        self.page.click("#react-burger-menu-btn")
        self.page.click("#logout_sidebar_link")