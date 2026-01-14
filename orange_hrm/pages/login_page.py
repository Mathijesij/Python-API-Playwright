from playwright.sync_api import Page
from ..locators.login_locators import LoginLocators as loc
from ..data import data
from ..resources.config import configuration
from ..resources.common_keywords import *


class LoginPage:
    """
    Page Object Model (POM) class that encapsulates all actions
    and behaviors related to the Login page.
    """

    def __init__(self, page: Page):
        """
        Initialize the LoginPage with a Playwright Page instance.

        :param page: Playwright Page object used to interact with the browser.
        """
        self.page = page
        self.ca = CommonActions(page)

    def goto(self):
        """
        Navigate to the application login page using the base URL
        from the configuration.
        """
        self.page.goto(configuration("URL", "base_url"))

    def navigate(self):
        self.page.goto(configuration("API_URL", "url"))

    def login(self):
        """
        Perform login using valid credentials from the test data.

        This method:
        - Enters the username into the username field
        - Enters the password into the password field
        - Clicks the Login button
        """
        self.ca.enter_value_by_placeholder(loc.username_placeholder, data.data["username"])
        self.ca.enter_value_by_placeholder(loc.password_placeholder, data.data["password"])
        self.ca.button(0, loc.login_btn_text)

        cookies = self.page.context.cookies()
        session_cookie_value = cookies[0]['value']
        # print(session_cookie_value)
        return session_cookie_value





