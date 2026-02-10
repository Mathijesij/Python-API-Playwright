from ..pages.pim_page import AddEmployee
from ..api.pim import PimApi
from ..pages.login_page import LoginPage


def test_add_new_employee(invoke_browser):
    """
    Test case: Add a new employee and fill in all required details.

    Steps:
    1. Navigate to PIM and create a new employee.
    2. Fill in personal details and custom fields.
    3. Enter contact details (address, telephone, email).
    4. Add emergency contact information.
    5. Add dependents for the employee.
    6. Enter immigration details.
    7. Update job-related details.
    8. Add salary information.

    :param invoke_browser: PyTest fixture that provides a Playwright page object.
    """

    # Initialize the page object
    page = invoke_browser
    pim = AddEmployee(page)

    # Add a new employee
    pim.add_employee()

    # Fill in personal and custom fields
    pim.new_user_personal_details()

    # Complete contact details
    pim.contact_details()

    # Add emergency contact information
    pim.emergency_contact()

    # Add dependents
    pim.dependants()

    # Add immigration information
    pim.immigration()

    # Add job-related details
    pim.job()

    # Add salary information
    pim.salary()

def test_api_add_employee(browserInvoke, api_request):
    """
    Test case to add a new employee via API and validate the addition via UI.

    Steps:
    1. Launch the application login page using the browser.
    2. Log in and retrieve the session cookie.
    3. Add a new employee using the PimApi.
    4. Validate that the employee was added by searching for the employee via the UI.

    Args:
        browserInvoke: Fixture or object to interact with the web browser.
        api_request: Fixture or object to make API requests.

    Returns:
        None
    """
    page = browserInvoke
    login_page = LoginPage(page)
    login_page.goto()

    session_cookie = login_page.login()

    pim_api = PimApi(api_request,
        session_cookie=session_cookie, page=page
    )

    employee_details = pim_api.add_new_emp()

    # for UI validation
    login_page = LoginPage(page)
    login_page.goto()

    pim_api.search_employee(employee_details["employeeId"],
                            employee_details["firstname"],
                            employee_details["middlename"],
                            employee_details["lastname"])


def test_api_add_personal_details(browserInvoke, api_request):
    """
    Test case to add personal details to a newly created employee via API.

    Steps:
    1. Launch the application login page using the browser.
    2. Log in and retrieve the session cookie.
    3. Add a new employee using the PimApi.
    4. Add personal details to the newly created employee.

    Args:
        browserInvoke: Fixture or object to interact with the web browser.
        api_request: Fixture or object to make API requests.

    Returns:
        None
    """
    page = browserInvoke
    login_page = LoginPage(page)
    login_page.goto()

    session_cookie = login_page.login()

    pim_api = PimApi(api_request, session_cookie=session_cookie, page=page)

    Emp_number = pim_api.add_new_emp()

    pim_api.add_personal_details(Emp_number["empNumber"])


def test_api_delete_employees(browserInvoke, api_request):
    """
    Test case to delete an employee via API and verify deletion via UI.

    Steps:
    1. Launch the application login page using the browser.
    2. Log in and retrieve the session cookie.
    3. Add a new employee using the PimApi.
    4. Delete the newly created employee using the API.
    5. Validate the deletion by searching for the deleted employee via the UI.

    Args:
        browserInvoke: Fixture or object to interact with the web browser.
        api_request: Fixture or object to make API requests.

    Returns:
        None
    """
    page = browserInvoke
    login = LoginPage(page)
    login.goto()

    session_cookie = login.login()

    pim_api = PimApi(api_request, session_cookie=session_cookie, page=page)

    Emp_number = pim_api.add_new_emp()

    pim_api.delete_employees(Emp_number["empNumber"])

    login_page = LoginPage(page)
    login_page.goto()

    pim_api.search_deleted_employee(Emp_number["employeeId"])

# pytest tests/test_orange_hrm.py::test_api_delete_employees --browser=chromium --headed
# pytest tests/test_orange_hrm.py::test_api_add_personal_details --browser=chromium --headed
# pytest tests/test_orange_hrm.py::test_api_add_employee --browser=chromium --headed
