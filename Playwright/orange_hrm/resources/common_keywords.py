from playwright.sync_api import Page, expect
from Playwright.orange_hrm.locators.common_locators import CommonLocators as CL
from ..locators.pim_locators import PIMLocators as PL
import string


class CommonActions:
    """
    A collection of common reusable UI actions for Playwright-based
    OrangeHRM automation tests.
    """

    def __init__(self, page: Page):
        """
        Initialize CommonActions with a Playwright Page instance.

        :param page: Playwright Page object used to interact with the browser.
        """
        self.page = page

    def navigate_to_pim(self):
        """
        Navigate to the PIM module by clicking the PIM menu item.
        """
        self.page.get_by_text(CL.pim_text).first.click()

    def verify_left_menu(self, expected_items):
        """
        Verify that all expected items are present in the left-side menu.

        :param expected_items: Iterable of expected menu item names.
        :raises AssertionError: If any expected menu items are missing.
        """
        self.page.wait_for_selector(CL.left_menu_css, timeout=10000)

        menu_items = self.page.locator(CL.left_menu_css).all_text_contents()
        menu_items = {item.strip() for item in menu_items if item.strip()}

        missing = set(expected_items) - menu_items
        assert not missing, f"Missing menu items: {missing}"

    def button(self, index, name):
        """
        Scroll into view and click a button identified by role and name.

        :param index: Zero-based index of the button.
        :param name: Accessible name of the button.
        """
        self.page.get_by_role("button", name=name).nth(index).scroll_into_view_if_needed()
        self.page.get_by_role("button", name=name).nth(index).click()

    def success_message(self):
        """
        Verify that a success message with text 'Success' is displayed.
        """
        success_msg = self.page.locator(CL.success_msg_css)
        expect(success_msg).to_have_text("Success")

    def input_text(self, label_name, value):
        """
        Enter text into an input field associated with a given label.

        :param label_name: Visible label text for the input field.
        :param value: Text value to be entered.
        """
        xpath = CL.input_text_xpath.replace('$$', f"'{label_name}'")
        self.page.locator(xpath).click()
        self.page.locator(xpath).fill(value)

    def get_input_text(self,  label_name):
        xpath = CL.input_text_xpath.replace('$$', f"'{label_name}'")
        return self.page.locator(xpath).input_value()

    def dropdown(self, value, role, name):
        """
        Select a value from a dropdown and choose an option by role and name.

        :param value: Visible text used to locate the dropdown.
        :param role: ARIA role of the dropdown option.
        :param name: Exact accessible name of the option to select.
        """
        xpath = CL.dropdown_xpath.replace('$$', f"'{value}'")
        self.page.locator(xpath).click()
        self.page.get_by_role(role, name=name, exact=True).click()

    def get_locator_by_placeholder(self, placeholder):

        return self.page.get_by_placeholder(placeholder)

    def get_value_by_placeholder(self, placeholder):

        return self.page.get_by_placeholder(placeholder).input_value()

    def enter_value_by_placeholder(self, placeholder, value):
        """
        Fill an input field identified by its placeholder text.

        :param placeholder: Placeholder text of the input field.
        :param value: Text value to be entered.
        """
        return self.page.get_by_placeholder(placeholder).fill(value)

    def enter_value_by_locator(self, locator, value):
        """
        Fill an input field using a locator string.

        :param locator: Playwright locator string.
        :param value: Text value to be entered.
        """
        return self.page.locator(locator).fill(value)

    def click_by_locator(self, locator):
        """
        Click an element identified by a locator string.

        :param locator: Playwright locator string.
        """
        return self.page.locator(locator).click()

    def select_employee_by_id(self, employee_id):

        xpath = PL.emp_xpath.replace('$$', f"'{employee_id}'")
        self.page.locator(xpath).click()

    def click_by_role(self, role, name):
        """
        Click an element using its ARIA role and accessible name.

        :param role: ARIA role of the element.
        :param name: Exact accessible name of the element.
        """
        return self.page.get_by_role(role, name=name, exact=True).click()

    def click_by_text(self, text):
        """
        Click an element identified by its visible text.

        :param text: Visible text of the element to click.
        """
        return self.page.get_by_text(text).click()

    def clear_input_field(self, locator):
        """
        Clear the value of an input field.

        :param locator: Playwright locator string.
        """
        return self.page.locator(locator).clear()

    def check_visibility_of_locator(self, locator):
        """
        Wait until an element becomes visible.

        :param locator: Playwright locator string.
        """
        return self.page.locator(locator).wait_for(state="visible")
