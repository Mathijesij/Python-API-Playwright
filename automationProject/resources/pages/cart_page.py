class CartPage:
    def __init__(self, page, locator):
        self.page = page
        self.locator = locator

    def proceed_to_checkout(self):
        self.page.locator(self.locator["proceed_to_checkout"]).click()
