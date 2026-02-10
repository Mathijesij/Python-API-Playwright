class AccountCreationPage:
    def __init__(self, page, locator, details):
        self.page = page
        self.locator = locator
        self.details = details

    def fill_account_info(self):
        self.page.locator(self.locator["title"]).set_checked(True)
        self.page.get_by_label(self.details["label_password"]).fill(self.details["password"])

        self.page.locator(self.locator["days"]).select_option(self.details["dob_day"])
        self.page.locator(self.locator["months"]).select_option(self.details["dob_month"])
        self.page.locator(self.locator["years"]).select_option(self.details["dob_year"])

        self.page.get_by_label(self.details["label_firstname"]).fill(self.details["first_name"])
        self.page.get_by_label(self.details["label_lastname"]).fill(self.details["last_name"])
        self.page.locator(self.locator["address1"]).fill(self.details["address"])
        self.page.locator(self.locator["country"]).select_option(self.details["country"])
        self.page.get_by_label(self.details["label_state"]).fill(self.details["state"])
        self.page.locator(self.locator["city"]).fill(self.details["city"])
        self.page.locator(self.locator["zipcode"]).fill(self.details["zipcode"])
        self.page.get_by_label(self.details["label_mobilenumber"]).fill(self.details["mobile_number"])

        self.page.get_by_role("button", name=self.details["create_acc_btn"]).click()

    def verify_account_created(self):
        return self.page.locator(self.locator["page_head_text"])

    def click_continue(self):
        self.page.get_by_text(self.details["continue_btn"]).click()
