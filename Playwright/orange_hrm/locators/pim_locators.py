class PIMLocators:
    # add new emp
    first_name_placeholder = "First Name"
    last_name_placeholder = "Last Name"
    emp_id_label_css = "input[class='oxd-input oxd-input--active']"
    togger_btn_css = "div.oxd-switch-wrapper span.oxd-switch-input"
    username_input_xpath = "//label[text()='Username']/parent::div/following-sibling::div//input"
    password_input_xpath = "//label[text()='Password']/parent::div/following-sibling::div//input"
    confirm_password_input_xpath = "//label[text()='Confirm Password']/parent::div/following-sibling::div//input"

    # select emp
    emp_xpath = "//div[@class='oxd-table-body']/div[contains(., $$)]"

    #personal details
    personal_details_header_css = "h6:has-text('Personal Details')"
    other_id_css = "div.oxd-input-group:has(label:has-text('Other Id')) input"
    driving_license_number_css ="div.oxd-input-group:has(label:has-text(\"Driver's License Number\")) input"
    license_expiry_date_css = "div.oxd-input-group:has(label:has-text('License Expiry Date')) input"
    nationality_css = "div.oxd-input-group:has(label:text('Nationality')) div.oxd-select-wrapper"
    marital_status_css = "div.oxd-input-group:has(label:text('Marital Status')) div.oxd-select-wrapper"
    dob_css = "div.oxd-input-group:has(label:has-text('Date of Birth')) input"
    gender_male_xpath = "//label[text()='Male']"
    gender_female_xpath = "//label[text()='Female']"

    # personal details - Custom Fields
    blood_type_css = "div.oxd-input-group:has(label:has-text('Blood Type')) .oxd-select-text-input"

    # contact details
    contact_details_text = "Contact Details"

    # emergency contacts
    emergency_contacts_text = "Emergency Contacts"

    # dependents
    dependents_text = "Dependents"

    # immigration
    immigration_text = "Immigration"

    # job
    job_text = "Job"

    #salary
    salary_text = "Salary"





