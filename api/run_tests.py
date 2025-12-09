# run_tests.py
import pytest
import datetime
import os

def run_tests():
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"report_{timestamp}.html"

    report_path = os.path.join(reports_dir, report_filename)  # ----> report directory & filename

    pytest_args = [
        "tests/",     # ----> path to file
        f"--html={report_path}",
        "--self-contained-html",
    ]
    pytest.main(pytest_args)

    print(f"Tests completed. HTML report generated at: {report_path}")

if __name__ == "__main__":
    run_tests()
