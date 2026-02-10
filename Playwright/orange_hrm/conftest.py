from .pages.login_page import LoginPage
import pytest
from datetime import datetime
import os
import inspect

# =========================
# Browser Invocation Fixture
# =========================
@pytest.fixture(scope="session")
def invoke_browser(playwright):
    """
    This fixture:
    - Launches the browser
    - Creates context and page
    - Logs into the application
    - Provides the page instance to tests
    """

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    login = LoginPage(page)
    login.goto()
    login.login()

    context.storage_state(path="auth.json")

    yield page

    # =========================
    # Teardown (after tests)
    # =========================
    page.close()
    context.close()
    browser.close()

# pytest tests/test_orange_hrm.py::test_api_add_employee --browser=chromium --headed

@pytest.fixture(scope="session")
def browserInvoke(browser):
    """
    browser: fixture from pytest-playwright
    Returns a page object
    """
    context = browser.new_context()
    page = context.new_page()

    yield page

    page.close()
    context.close()

# =========================
# Pytest HTML Report Configuration
# =========================
def pytest_configure(config):
    """
    This hook configures pytest-html reporting:
    - Generates timestamped HTML reports
    - Saves reports inside 'reports' folder
    """

    # Generate current timestamp for report name
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Get the directory of the current file (orange_hrm folder)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Create 'reports' directory inside orange_hrm if not exists
    reports_dir = os.path.join(base_dir, "reports")
    os.makedirs(reports_dir, exist_ok=True)

    # Define full report file path
    report_path = os.path.join(reports_dir, f"report_{now}.html")

    # Set pytest-html report output path
    config.option.htmlpath = report_path

    # Enable self-contained HTML report (CSS & JS embedded)
    config.option.self_contained_html = True

@pytest.fixture
def api_request(playwright, request):
    """Provides a Playwright api request context for tests."""
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to capture a screenshot when a test fails.

    This hook is executed after each test phase ('setup', 'call', 'teardown').
    It captures a screenshot only if the test itself (the 'call' phase) fails.

    Args:
        item: The pytest test item object. Provides access to test function, name, and fixtures.
        call: The test call object. Contains information about the test phase and outcome.

    Behavior:
        - Only captures screenshots during the 'call' phase if the test failed.
        - Attempts to retrieve a `browserInvoke` fixture (expected to be a Playwright page object).
        - If the page is available, saves a screenshot to the "screenshots" folder with a timestamp.
        - Skips screenshot for API-only tests or if the page fixture is not present.
    """
    outcome = yield
    rep = outcome.get_result()

    # Only take screenshot if test itself failed
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("browserInvoke")

        # API-only tests will not have a page
        if not page:
            return
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        screenshot_path = f"screenshots/{item.name}_{timestamp}.png"
        page.screenshot(path=screenshot_path, full_page=True)

