import json
from playwright.sync_api import Page, expect
from ..resources.api_utils import ApiUtils
from ..resources.config import configuration
from ..resources.resources import resources
from ..pages.login_page import LoginPage
from ..pages.pim_page import AddEmployee

base_url = configuration("API_URL", "url")


class PimApi:
    """
    A utility class for interacting with the OrangeHRM API and automating
    related UI validations using Playwright.

    This class provides methods to:
        - Add a new employee via API
        - Update personal details of an employee
        - Delete employees via API
        - Search for an employee and validate details in the UI
        - Search for a deleted employee and validate no records found

    Attributes:
        page (Page): Playwright page object for UI interactions.
        data (resources): Resource helper instance for generating random data.
        api_utils (ApiUtils): Helper instance to make API requests (GET, POST, PUT, DELETE).
        session_cookie (str): Session cookie string for authentication in API requests.
        pim_page (AddEmployee): Page object for PIM-related UI operations.
    """

    def __init__(self, api_request, session_cookie, page: Page):
        """
        Initialize the API helper class.

        Args:
            api_request: Object to make API requests (used by ApiUtils).
            session_cookie (str): Authentication cookie for API requests.
            page (Page): Playwright page object.
        """
        self.page = page
        self.data = resources()
        self.api_utils = ApiUtils(api_request)
        self.session_cookie = session_cookie
        self.pim_page = AddEmployee(page)

    def add_new_emp(self):
        """
        Add a new employee via API.

        Generates random employee data, sends a POST request to the
        `/pim/employees` endpoint, and validates the response.

        Returns:
            dict: Employee details including empNumber, employeeId, first/middle/last name.
        """
        data = {
            "firstName": self.data.generate_first_name(),
            "middleName": self.data.generate_first_name(),
            "lastName": self.data.generate_last_name(),
            "employeeId": self.data.random_emp_id()
        }

        url = f'{base_url}/api/v2/pim/employees'

        headers = {
            "Cookie": f"orangehrm={self.session_cookie}",
            "Content-Type": "application/json"
        }

        response = self.api_utils.post_method(url=url, data=data, headers=headers)
        res_json = response.json()

        # Validate response
        assert "data" in res_json
        assert "empNumber" in res_json["data"]
        emp_number = res_json["data"]["empNumber"]
        assert emp_number is not None and isinstance(emp_number, int)

        employee_id = res_json["data"]["employeeId"]
        emp_first_name = res_json["data"]["firstName"]
        emp_middle_name = res_json["data"]["middleName"]
        emp_last_name = res_json["data"]["lastName"]

        return {
            "empNumber": emp_number,
            "employeeId": employee_id,
            "firstname": emp_first_name,
            "middlename": emp_middle_name,
            "lastname": emp_last_name
        }

    def add_personal_details(self, get_empNumber):
        """
        Update personal details of an employee.

        Sends a PUT request to `/pim/employees/{empNumber}/personal-details`
        with random personal details including gender, marital status, and nationality.

        Args:
            get_empNumber (int): The employee number to update.

        Raises:
            AssertionError: If response status is not 200.
        """
        data = {
            "firstName": self.data.generate_first_name(),
            "middleName": self.data.generate_first_name(),
            "lastName": self.data.generate_first_name(),
            "employeeId": self.data.random_emp_id(),
            "gender": 1,
            "maritalStatus": self.data.marital_status(),
            "nationalityId": 82
        }

        url = f'{base_url}/api/v2/pim/employees/{get_empNumber}/personal-details'

        headers = {
            "Cookie": f"orangehrm={self.session_cookie}",
            "Content-Type": "application/json"
        }

        response = self.api_utils.put_method(url=url, data=data, headers=headers)
        assert response.status == 200
        assert response.status_text == "OK"

    def delete_employees(self, emp_number):
        """
        Delete an employee via API.

        Args:
            emp_number (int): The employee number to delete.

        Raises:
            AssertionError: If the delete operation fails.
        """
        url = f"{base_url}/api/v2/pim/employees"
        headers = {
            "Cookie": f"orangehrm={self.session_cookie}",
            "Content-Type": "application/json"
        }
        payload = {"ids": [emp_number]}

        response = self.api_utils.delete_method(url=url, headers=headers, data=payload)
        assert response.status == 200
        assert response.status_text == "OK"

    def search_employee(self, employeeId, firstname, middlename, lastname):
        """
        Search for an employee in the UI and validate fields.

        Args:
            employeeId (int): Employee ID to search.
            firstname (str): Expected first name.
            middlename (str): Expected middle name.
            lastname (str): Expected last name.

        Raises:
            AssertionError: If any field does not match expected value.
        """
        self.pim_page.search_emp(employeeId)
        expected_data = self.pim_page.validate_the_fields()

        assert expected_data["first_name"] == firstname
        assert expected_data["middle_name"] == middlename
        assert expected_data["last_name"] == lastname
        assert expected_data["emp_id"] == employeeId

    def search_deleted_employee(self, employeeId):
        """
        Search for a deleted employee in the UI and verify no records are found.

        Args:
            employeeId (int): Employee ID to search.
        """
        self.pim_page.search_deleted_emp(employeeId)
        self.pim_page.no_records_found_toast()
