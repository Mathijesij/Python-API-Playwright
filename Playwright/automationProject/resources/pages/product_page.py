class ProductPage:
    def __init__(self, page, locator):
        self.page = page
        self.locator = locator

    def click_saree(self):
        self.page.locator(self.locator["saree"]).click()

    def open_first_product(self):
        self.page.locator(self.locator["first_product"]).click()

    def add_to_cart(self):
        self.page.locator(self.locator["add_to_cart"]).click()

    def view_cart(self):
        self.page.locator(self.locator["view_cart"]).click()
