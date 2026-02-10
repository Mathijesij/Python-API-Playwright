from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page, locator, details):
        self.page = page
        self.locator = locator
        self.details = details

    def goto_home(self):
        self.page.goto(self.details["url"])

    def click_signup_login(self):
        self.page.get_by_text(self.details["signup_or_login"]).click()

    def displayed_user_visible(self):
        return self.page.locator(self.locator["displayed_user_name"])

    def click_women_category(self):
        self.page.locator(self.locator["women"]).click()
