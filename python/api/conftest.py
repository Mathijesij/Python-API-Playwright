import pytest
import datetime
import os

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
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

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
