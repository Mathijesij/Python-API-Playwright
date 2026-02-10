import time
from playwright.sync_api import Page, expect
from ..resources.common_keywords import CommonActions
from ..locators.common_locators import CommonLocators as CL
from ..locators.pim_locators import PIMLocators as PL
from ..data import data
from ..resources.resources import resources


class AddEmployee:
    """
    Page Object Model (POM) class that handles all employee-related actions,
    including adding a new employee and updating their personal, job,
    salary, and related details.
    """

    def __init__(self, page: Page):
        """
        Initialize AddEmployee with a Playwright Page instance.

        :param page: Playwright Page object used to interact with the browser.
        """
        self.page = page
        self.res = resources()
        self.ca = CommonActions(page)

    def enter_details(self):
        """
        Add a new employee by entering basic details such as name,
        employee ID, and login credentials, then save the record.
        """
        self.ca.button(0, CL.add_button)

        self.ca.enter_value_by_placeholder(PL.first_name_placeholder, self.res.generate_first_name())
        self.ca.enter_value_by_placeholder(PL.last_name_placeholder, self.res.generate_last_name())
        self.ca.clear_input_field(PL.emp_id_label_css)
        self.ca.enter_value_by_locator(PL.emp_id_label_css, self.res.random_emp_id())

        self.ca.click_by_locator(PL.togger_btn_css)

        self.ca.enter_value_by_locator(PL.username_input_xpath, self.res.generate_username())
        self.ca.enter_value_by_locator(PL.password_input_xpath, data.data["emp_password"])
        self.ca.enter_value_by_locator(PL.confirm_password_input_xpath, data.data["confirm_password"])

        self.ca.button(0, CL.save_button)

    def search_emp(self, employee_id):
        """
        Search for an employee using the employee ID
        and open the employee record.
        """
        self.ca.navigate_to_pim()

        self.ca.input_text("Employee Id", employee_id)

        self.ca.button(0, "Search")

        self.ca.select_employee_by_id(f'{employee_id}')

    def search_deleted_emp(self, employee_id):
        self.ca.navigate_to_pim()

        self.ca.input_text("Employee Id", employee_id)

        self.ca.button(0, "Search")

    def no_records_found_toast(self):
        toast = (
            self.page.locator(CL.no_record_found_message_css)
            .get_by_text(CL.no_record_found_message)
        )

        expect(toast).to_be_visible()

    def validate_the_fields(self):
        first_name = self.ca.get_locator_by_placeholder("First Name")
        expect(first_name).not_to_have_value("")

        return {
            "first_name": self.ca.get_value_by_placeholder("First Name"),
            "middle_name": self.ca.get_value_by_placeholder("Middle Name"),
            "last_name": self.ca.get_value_by_placeholder("Last Name"),
            "emp_id": self.ca.get_input_text("Employee Id")
        }

    def personal_details(self):
        """
        Update and save employee personal details such as
        nationality, marital status, date of birth, and gender.
        """
        self.ca.check_visibility_of_locator(PL.personal_details_header_css)

        self.ca.click_by_locator(PL.other_id_css)
        self.ca.enter_value_by_locator(PL.other_id_css, self.res.random_other_id())

        self.ca.click_by_locator(PL.driving_license_number_css)
        self.ca.enter_value_by_locator(PL.driving_license_number_css, self.res.random_license_number())

        self.ca.enter_value_by_locator(PL.license_expiry_date_css, self.res.generate_license_expiry())

        self.ca.dropdown("Nationality", "option", data.data["nationality"])
        self.ca.dropdown("Marital Status", "option", self.res.marital_status())

        self.ca.enter_value_by_locator(PL.dob_css, data.data["dob"])

        gender = self.res.gender()
        if gender == "Male":
            self.ca.click_by_locator(PL.gender_male_xpath)
        elif gender == "Female":
            self.ca.click_by_locator(PL.gender_female_xpath)

        self.ca.button(0, CL.save_button)

        self.ca.success_message()

    def custom_fields(self):
        """
        Update and save employee custom fields such as
        blood type and additional test fields.
        """
        self.ca.dropdown("Blood Type", "option", self.res.blood_type())
        self.ca.input_text("Test_Field", self.res.test_field())
        self.ca.button(1, CL.save_button)
        self.ca.success_message()

    def contact_details_address(self):
        """
        Enter employee contact address details including
        street, city, state, zip code, and country.
        """
        self.ca.click_by_text(PL.contact_details_text)

        self.ca.input_text("Street 1", data.data["street_1"])
        self.ca.input_text("Street 2", data.data["street_2"])
        self.ca.input_text("City", data.data["city"])
        self.ca.input_text("State/Province", data.data["state"])
        self.ca.input_text("Zip/Postal Code", data.data["zip_code"])
        self.ca.dropdown("Country", "option", data.data["country"])

    def contact_details_telephone(self):
        """
        Enter employee telephone contact details
        such as home, mobile, and work numbers.
        """
        self.ca.input_text("Home", self.res.contact_number())
        self.ca.input_text("Mobile", self.res.contact_number())
        self.ca.input_text("Work", self.res.contact_number())

    def contact_details_email(self):
        """
        Enter employee email details and save the contact information.
        """
        self.ca.input_text("Work Email", self.res.generate_work_email())
        self.ca.input_text("Other Email", self.res.generate_other_email())

        self.ca.button(0, CL.save_button)
        self.ca.success_message()

    def emergency_contacts(self):
        """
        Add and save an emergency contact for the employee.
        """
        self.ca.click_by_text(PL.emergency_contacts_text)

        self.ca.button(0, CL.add_button)

        self.ca.input_text("Name", self.res.generate_name())
        self.ca.input_text("Relationship", self.res.relationship())
        self.ca.input_text("Home Telephone", self.res.contact_number())
        self.ca.input_text("Mobile", self.res.contact_number())
        self.ca.input_text("Work Telephone", self.res.contact_number())

        self.ca.button(0, CL.save_button)
        self.ca.success_message()

    def depent(self):
        """
        Add and save a dependent for the employee.
        """
        self.ca.click_by_text(PL.dependents_text)

        self.ca.button(0, CL.add_button)

        self.ca.input_text("Name", self.res.generate_name())

        relationship = self.res.dependents_relationship()
        self.ca.dropdown("Relationship", "option", relationship)

        if relationship == "Other":
            self.ca.input_text("Please Specify", self.res.test_field())

        self.ca.input_text("Date of Birth", data.data["dependants_dob"])

        self.ca.button(0, CL.save_button)

    def pim_immigration(self):
        """
        Add and save employee immigration details.
        """
        self.ca.click_by_text(PL.immigration_text)

        self.ca.button(0, CL.add_button)

        self.ca.input_text("Number", self.res.random_other_id())
        self.ca.input_text("Issued Date", self.res.generate_random_past_date())

        self.ca.button(0, CL.save_button)
        self.ca.success_message()

    def pim_job(self):
        """
        Update and save employee job-related details such as
        job title, category, location, and employment status.
        """
        self.ca.click_by_text(PL.job_text)

        self.ca.input_text("Joined Date", self.res.generate_random_past_date())
        self.ca.dropdown("Job Title", "option", self.res.job_title())
        self.ca.dropdown("Job Category", "option", self.res.job_category())
        self.ca.dropdown("Sub Unit", "option", self.res.sub_unit())
        self.ca.dropdown("Location", "option", self.res.location())

        emp_status = self.res.emp_status()
        self.ca.dropdown("Employment Status", "option", emp_status)

        if emp_status in ["Full-Time Contract", "Part-Time Contract"]:
            self.ca.click_by_locator(PL.togger_btn_css)
            self.ca.input_text("Contract Start Date",self.res.generate_random_past_date())
            self.ca.input_text("Contract End Date",self.res.generate_license_expiry())

        self.ca.button(0, CL.save_button)
        self.ca.success_message()

    def pim_salary(self):
        """
        Add and save employee salary details based on pay grade.
        """
        self.ca.click_by_text(PL.salary_text)

        self.ca.button(0, CL.add_button)

        self.ca.input_text("Salary Component", data.data["salary_component"])
        grade = self.res.pay_grade()
        self.ca.dropdown("Pay Grade", "option", grade)
        self.ca.dropdown("Pay Frequency", "option", self.res.pay_frequency())
        self.ca.dropdown("Currency", "option", data.data["currency"])

        if grade == "Grade 1":
            self.ca.input_text("Amount", self.res.grade1_amount())
        elif grade == "Grade 2":
            self.ca.input_text("Amount", self.res.grade2_amount())
        elif grade == "Grade 3":
            self.ca.input_text("Amount", self.res.grade3_amount())
        elif grade == "Grade 4":
            self.ca.input_text("Amount", self.res.grade4_amount())
        elif grade == "Grade 5":
            self.ca.input_text("Amount", self.res.grade5_amount())

        self.ca.button(0, CL.save_button)

    def add_employee(self):
        """
        Validate the left menu, navigate to PIM,
        and initiate the employee creation process.
        """
        expected_menu = {
            "Admin", "PIM", "Leave", "Time", "Recruitment", "My Info",
            "Performance", "Dashboard", "Directory", "Maintenance",
            "Claim", "Buzz"
        }
        self.ca.verify_left_menu(expected_menu)
        self.ca.navigate_to_pim()
        self.enter_details()

    def new_user_personal_details(self):
        """
        Complete personal details and custom fields
        for a newly added employee.
        """
        self.personal_details()
        self.custom_fields()

    def contact_details(self):
        """
        Complete all employee contact details including
        address, telephone, and email information.
        """
        self.contact_details_address()
        self.contact_details_telephone()
        self.contact_details_email()

    def emergency_contact(self):
        """
        Add emergency contact details for the employee.
        """
        self.emergency_contacts()

    def dependants(self):
        """
        Add dependent details for the employee.
        """
        self.depent()

    def immigration(self):
        """
        Add immigration details for the employee.
        """
        self.pim_immigration()

    def job(self):
        """
        Add or update job-related information for the employee.
        """
        self.pim_job()

    def salary(self):
        """
        Add or update salary information for the employee.
        """
        self.pim_salary()
