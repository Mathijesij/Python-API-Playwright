class CheckoutPage:
    def __init__(self, page, locator):
        self.page = page
        self.locator = locator

    def place_order(self):
        self.page.locator(self.locator["place_order"]).click()
