class SignupLoginPage:
    def __init__(self, page, locator, details):
        self.page = page
        self.locator = locator
        self.details = details

    def signup(self):
        self.page.get_by_placeholder(self.details["name"]).fill(self.details["user_name"])
        self.page.locator(self.locator["sign_up_email"]).fill(self.details["user_email"])
        self.page.get_by_role("button", name=self.details["signup_btn"]).click()
