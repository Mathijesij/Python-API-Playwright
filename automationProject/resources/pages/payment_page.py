class PaymentPage:
    def __init__(self, page, locator, details):
        self.page = page
        self.locator = locator
        self.details = details

    def fill_payment_details(self):
        self.page.locator(self.locator["name_on_card"]).fill(self.details["name_on_card"])
        self.page.locator(self.locator["card_number"]).fill(self.details["card_number"])
        self.page.locator(self.locator["cvc"]).fill(self.details["cvc"])
        self.page.locator(self.locator["expire_month"]).fill(self.details["exp_month"])
        self.page.locator(self.locator["expire_year"]).fill(self.details["exp_year"])

        self.page.get_by_role("button", name=self.details["pay_and_order_btn"]).click()

    def verify_order_placed(self):
        return self.page.locator(self.locator["page_head_text"])
