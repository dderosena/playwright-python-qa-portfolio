class CheckoutPage:
    def __init__(self, page):
        self.page = page
    
    def enter_customer_info(self, first_name, last_name, postal_code):
        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", postal_code)

    def continue_checkout(self):
        self.page.click("#continue")
    
    def finish_checkout(self):
        self.page.click("#finish")
        