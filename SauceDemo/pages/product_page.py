class ProductPage:
    def __init__(self, page):
        self.page = page

    def open_backpack(self):
        self.page.click("#item_4_title_link")