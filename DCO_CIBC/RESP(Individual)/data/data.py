# common data
url = 'https://m.sit1.onlinebrokerage.cibc.com/dco/#/accountOpenPreLogin'
browser = 'chrome'
time_out = '15s'
accept_all_cookies_btn = 'Accept all cookies'
start_application_btn = 'Start application'
next_btn = 'Next'
edit_btn = 'Edit'
back_btn = 'Back'
confirm_btn = 'Confirm'
lets_go_btn = "Let’s go"

data_file_path = "C:/Users/MathijesiJohnbritto/PycharmProjects/demo/DCO_CIBC/RESP(Individual)/data/input/input_fields.csv"
screenshot_path = "C:/Users/MathijesiJohnbritto/PycharmProjects/demo/DCO_CIBC/RESP(Individual)/data/capturedScreenshot/"

# error message data
error_message_text = 'xpath://div[@class="errorMessage" and contains(text(),"$$")]'

# introduce yourself page
title_error_msg = 'Select a title.'
first_name_error_msg = 'First name is missing.'
invalid_name_error_msg = "You've used invalid characters."
last_name_error_msg = 'Last name is missing.'
sin_error_msg = 'Enter a valid SIN.'
invalid_sin_error_msg = "You've entered an invalid Social Insurance Number."
email_error_msg = 'Enter a valid email address.'
mobile_error_msg = "You've entered an invalid phone number. Enter a 10 digit number."
address_error_msg = 'Address is missing.'
city_error_msg = 'City of residence is missing.'
province_error_msg = 'Select your province of residence.'
postal_code_error_msg = 'Enter a valid postal code.'

# taxpayer information page
country_of_citizenship_error_msg = 'Select your country of citizenship.'
country_of_residence_error_msg = 'Select your country of residence.'

# marital status page
spouse_title_error_msg = 'Select a title that best suits your spouse.'
spouse_first_name_error_msg = "Spouse's first name is missing."
spouse_invalid_name_error_msg = "You've used invalid characters."
spouse_last_name_error_msg ="Spouse's last name is missing."
spouse_employment_status_error_msg = "Select the option that best suits your spouse's employment status."
spouse_employer_name_error_msg = "Enter spouse's employer's name."
spouse_valid_description_error_msg = "You need to enter a valid description of your business."

# finicial details
amount_field_error_msg = "Enter an amount of zero or greater."
source_income_error_msg = "Oops! Try again. You need to specify the source of your annual income."
years_of_investing_error_msg = "Enter the number of years you have been investing."
invalid_years_of_investing_error_msg = "You've entered too many characters."

# bank information
select_bank_info_error_msg = "Select one option."

# resp beneficiary details
relationship_to_you_error_msg = "Select a term that best describes the beneficiary's relationship to you."
beneficiary_title_error_msg = "Select a title that best suits the beneficiary."
beneficiary_first_name_error_msg = "Beneficiary's first name is missing."
beneficiary_last_name_error_msg = "Beneficiary's last name is missing."
beneficiary_dob_month_error_msg = "Select the beneficiary's month of birth."
beneficiary_dob_day_error_msg = "Enter the beneficiary's day of birth."
beneficiary_dob_year_error_msg = "Enter the beneficiary's year of birth."
beneficiary_gender_error_msg = "Select the beneficiary's gender."
beneficiary_sin_error_msg = "Enter a valid SIN for your beneficiary."
beneficiarys_address_error_msg =  "Select an option."
# if diff
beneficiary_address_error_msg = "Beneficiary's address is missing."
beneficiary_city_error_msg = "City of residence is missing."
beneficiary_province_error_msg = "Select a province of residence."
beneficiary_postal_code_error_msg = "Enter a valid postal code."
beneficiary_under_19_year_error_msg = "Select either Yes or No."

# resp_education_and_funding_page
cesg_error_msg = "Select either Yes or No."
additional_error_msg = "Select either Yes or No."
canada_learning_bond_error_msg = "Select either Yes or No."

custom_user_id_error_msg = "User ID is required information."
sign_on_password_error_msg = "New sign on password is required information."

re_enter_sign_on_password = "Passwords don’t match"

option_trading_password = "You haven’t chosen an option for your trading password. Let’s try again."

go_green_go_paperless = "Select one option."


# validate data
# introduce yourself
# for validate the entered details in introduce yourself
entered_name = 'Name:'
entered_email_address = 'Email address:'
entered_dob = 'Date of birth:'
entered_sin = 'SIN:'
entered_mobile_number = 'Mobile phone number:'
entered_address = 'Address:'
selected_preferred_language = 'Preferred language:'


# custom acc resp account
after_yes = "You are applying to purchase Calls and Puts, and Covered Writing."
after_no = "You can also apply for Option Trading Privileges after your account is open."
