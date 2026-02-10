# common objects
navigation_button =     "xpath://button[normalize-space(text())='$$']"
yes =       "xpath://div[contains(@id,'yes')]"
no =        "xpath://div[contains(@id,'no')]"
select_object = "xpath://option[normalize-space(text())='$$']"
# -------------------------------------------------------------------------------------

# open an investors edge account page
dont_have_acc ="xpath://input[@id='unauth-option']"

# ------------------------------------------------------------------------------------------

# before we begin page
understand_and_agree_checkbox =    "xpath://input[contains(@class,'checkbox userConcent')]"

# ------------------------------------------------------------------------------------------

# choose your account page
select_resp =      "xpath://input[@id='respAccount']"
individual_resp =      "xpath://input[@value='RSP']"

# ------------------------------------------------------------------------------------------
# Application info -> Introduce yourself

# Personal Information
title="xpath://select[@id='title_select']"
first_name="xpath://input[@id='first_name']"
middle_name="xpath://input[@id='middle_name']"
last_name="xpath://input[@id='last_name']"
preferred_name="xpath://input[@id='preferred_name']"
dob_month="xpath://select[@id='primary_dob_month']"
select_dob_month = "xpath://select[@id='primary_dob_month']/option[normalize-space(text())='$$']"
dob_day="xpath://input[@id='primary_dob_day']"
dob_year="xpath://input[@id='primary_dob_year']"
sin="xpath://input[@id='sin_input']"
sin_expire_month = "xpath://select[@id='sin_expiry_month']"
select_exp_month = "xpath://select[@id='sin_expiry_month']/option[normalize-space(text())='$$']"
sin_expire_day = "xpath://input[@id='sin_expiry_day']"
sin_expire_year = "xpath://input[@id='sin_expiry_year']"
# sin expired month day year

# contact information
email_address="xpath://input[@id='email_input']"
mobile_phone_number="xpath://input[contains(@id,'primaryPhone')]"
home_phone_number="xpath://input[contains(@id,'secondaryPhone')]"

# address information
address_including_unit="xpath://input[@id='addressInput']"
select_base_on_unit = "xpath://span[@class='address-text' and contains(text(),'$$')]"
city="xpath://input[@id='cityInput']"
province="xpath://select[@id='provinceSelect']"
# select_province="xpath://option[normalize-space(text())='$$']"
postal_code="xpath://input[@id='postalCodeInput']"
same_mailing_address_checkbox="xpath://div[contains(@id,'sameAddress_label')]"

# mailing address
mailing_address="xpath://input[@id='mailAddressInput']"
mailing_city="xpath://input[@id='mailCityInput']"
mailing_province="xpath://select[@id='mailProvinceSelect']"
# mailing_select_province="xpath://option[normalize-space(text())='$$']"
mailing_postal_code="xpath://input[@id='mailPostalCodeInput']"

# language preferred
english="xpath://span[normalize-space(text())='English']"
french="xpath://span[normalize-space(text())='French']"

# validate the enter details
validate_entered_name="xpath://span[text()='Name:']/following::span[1]"
validate_entered_email = "xpath://span[text()='Email address:']/following::span[1]"
validate_entered_sin = "xpath://span[text()='SIN:']/following::span[1]"
validate_entered_phone = "xpath://span[text()='Mobile phone number:']/following::span[1]"
validate_entered_address = "xpath://span[text()='Address:']/following::span[1]"
validate_entered_dob = "xpath://span[text()='Date of birth:']/following::span[1]"

# Application info -> Taxpayer Information
canadian_citizen = "xpath://fieldset[@id='cadcitizen']//span[normalize-space(text())='$$']"
country_of_citizenship =        "xpath://select[@id='country-dd']"
# select_country_of_citizenship =     "xpath://option[normalize-space(text())='$$']"
resident_of_canada = "xpath://fieldset[@id='cadresident']//span[normalize-space(text())='$$']"
country_of_residency =      "xpath://select[@id='res-country-dd']"
# select_country_of_residency =       "xpath://option[normalize-space(text())='$$']"

# next_btnnn = ""

# Application info -> Marital Status
spouse_common_law_partner_yes =  "xpath://input[@id='spouse-radio-yes']"
spouse_common_law_partner_no = "xpath://input[@id='spouse-radio-no']"
spouse_title =     "xpath://select[@id='spouse-title']"

# select_spouse_title =  "xpath://option[normalize-space(text())='$$']"
spouse_first_name =    "xpath://input[@id='spouse-first-name']"
spouse_middle_name =   "xpath://input[@id='spouse-middle-name']"
spouse_last_name =     "xpath://input[@id='spouse-last-name']"
spouse_employment_status =     "xpath://select[@id='spouse-employementTypes']"
select_spouse_employment_status =  "xpath://option[normalize-space(text())='$$]"

# first 3 option
spouse_employer_name =     "xpath://input[@id='spouse-employer-name']"

# if self employee
nature_of_business =     "xpath://input[@id='spouse-nature-of-business']"

# Application info -> Employment Status
employment_status = "xpath://select[@id='employmentStatus']"
type_of_business = "xpath://select[@id='occupationCategory_select']"
# select_type_of_business = "xpath://option[normalize-space(text())='$$']"
occupation = "xpath://select[@id='occupations_select']"
# select_occupation = "xpath://option[normalize-space(text())='$$']"
employer_name = "xpath://input[@id='employerName_input']"
employer_address = "xpath://input[@id='addressInput']"
employer_city = "//input[@id='cityInput']"
state_province_emp_status = "xpath://select[@id='provinceSelect']"
# select_province_emp_status = "xpath://option[normalize-space(text())='$$']"
# bck_button$e
# next btn

# Application info -> Financial Details
household_liquid_asset = "xpath://input[@id='liquidAssets_input']"
household_fixed_asset = "xpath://input[@id='fixedAssets_input']"
household_liabilities = "xpath://input[@id='liabilities_input']"

# get details
displayed_total_assert = "xpath://div[@class='estimateBorder']//child::div[1]/label"
displayed_liabilities = "xpath://div[@class='estimateBorder']//child::div[2]/label"
displayed_total_net_worth = "xpath://div[@class='estimateBorder']//child::div[3]/label"

annual_income = "xpath://input[@id='annualIncome_input']"
annual_income_source = "xpath://select[@id='annualIncomeSource_input']"
# select_annual_income_source = "xpath://option[normalize-space(text())='$$']"

years_of_investing = "xpath://input[@id='yearsInvestingInput']"

# if click other in source
more_information = "xpath://input[@id='moreInfo_input']"

# Application info -> Bank Information
dont_link_a_bank_acc = "xpath://input[@id='link_acc_radio-no']"
# next btn

# ------------------------------------------------------------------------------------------
# Customize account -> RESP account
# select yes or no
option_trading_privileges = "xpath://p[contains(text(),'apply for Option Trading Privileges?')]"
#nextbtn

# Customize account -> RESP beneficiary information
relationship_to_you = "xpath://select[@id='respBene_relationship_select0']"
# select_relationship_to_you = "xpath://option[normalize-space(text())='$$']"
beneficiary_title = "xpath://select[@id='title_select0']"
# select_beneficiary_title = "xpath://option[normalize-space(text())='$$']"
beneficiary_first_name = "xpath://input[@id='first_name0']"
beneficiary_last_name = "xpath://input[@id='last_name0']"
beneficiary_dob_month = "xpath://select[@id='primary_dob_month0']"
# select_beneficiary_dob_month = "xpath://option[normalize-space(text())='$$']"
beneficiary_dob_day = "xpath://input[@id='primary_dob_day0']"
beneficiary_dob_year = "xpath://input[@id='primary_dob_year0']"
beneficiary_gender = "xpath://select[@id='genderSelect0']"
# select_beneficiary_gender = "xpath://option[normalize-space(text())='$$']"
beneficiary_sin = "xpath://input[@id='sin_input0']"
beneficiary_sin_month = "xpath://select[@id='sin_expiry_month0']"
beneficiary_sin_day = "xpath://input[@id='sin_expiry_day0']"
beneficiary_sin_year = "xpath://input[@id='sin_expiry_year0']"
beneficiary_resident_of_canada_yes = "xpath://input[@id='radio-cadResident-yes0']"
beneficiary_resident_of_canada_no = "xpath://input[@id='radio-cadResident-no0']"
beneficiary_address_same_as_sub ="xpath://input[@id='radio-address-yes0']"
beneficiary_address_diff_than_sub = "xpath://input[@id='radio-address-no0']"
# if diff
beneficiary_address = "xpath://input[@id='addressInput0']"
beneficiary_city = "xpath://input[@id='cityInput0']"
beneficiary_province = "xpath://select[@id='provinceSelect0']"
beneficiary_select_province = "xpath://option[normalize-space(text())='$$']"
beneficiary_postal_code = "xpath://input[@id='postalCodeInput0']"
# is beneficiary is under 19 year age yes or no
below_age = "xpath://input[@id='radio-minor-yes0']"
above_age = "xpath://input[@id='radio-minor-no0']"
# after yes there is other yes or no
# next btn

# Customize account -> RESP education and funding
cesg_yes = "xpath://div[contains(@id,'radio-cesg-choice-yes')]"
cesg_no = "xpath://div[contains(@id,'radio-cesg-choice-no')]"

additional_cesg_yes = "xpath://div[contains(@id,'radio-add-cesg-choice-yes')]"
additional_cesg_no = "xpath://div[contains(@id,'radio-add-cesg-choice-no')]"

canada_learning_bond_yes = "xpath://input[@id='radio-clb-choice-yes']"
canada_learning_bond_no = "xpath://input[@id='radio-clb-choice-no']"

designated_education_institution = "xpath://input[@id='educationalInstitute_label']"

# ------------------------------------------------------------------------------------------
# review -> Final Question page
user_alone_or_as_part_of_a_group_hold_yes = "xpath://input[@id='radio-primary-ctrl-yes']"
user_alone_or_as_part_of_a_group_hole_no = "xpath://input[@id='radio-primary-ctrl-no']"

spouse_alone_or_as_part_of_a_group_hold_yes = "xpath://input[@id='radio-spouse-ctrl-yes']"
spouse_alone_or_as_part_of_a_group_hole_no = "xpath://input[@id='radio-spouse-ctrl-no']"

reporting_issue_or_other_issue_yes = "xpath://input[@id='radio-primary-insider-yes']"
reporting_issue_or_other_issue_no = "xpath://input[@id='radio-primary-insider-no']"

spouse_reporting_issue_or_other_issue_yes = "xpath://input[@id='radio-spouse-insider-yes']"
spouse_reporting_issue_or_other_issue_no = "xpath://input[@id='radio-spouse-insider-no']"

living_in_same_home_yes = "xpath://input[@id='radio-primary-Pro-yes']"
living_in_same_home_no = "xpath://input[@id='radio-primary-Pro-no']"

spouse_living_in_same_home_yes = "xpath://input[@id='radio-spouse-Pro-yes']"
spouse_living_in_same_home_no = "xpath://input[@id='radio-spouse-Pro-no']"

i_do_not_object = "xpath://div[contains(@id, 'radio-objection-yes')]"
i_do_object = "xpath://div[contains(@id, 'radio-objection-no')]"

security_holder_material_no = "xpath://div[contains(@id,'radio-security-none')]"
security_holder_material_yes = "xpath://div[contains(@id,'radio-security-all')]"
proxy_related_material_yes = "xpath://div[contains(@id,'radio-security-some')]"

# next or back btn

# review -> review information page

display_details_in_review="xpath:(//label[normalize-space(text())='$$'])[1]/following::p[1]"
# Name:
# Email address:
# Mobile phone number:
# Address:
# Employment Status:
# Annual income:
# Net worth:
# Source of annual income:

review_occupation = "xpath://label[text()='Occupation:']/following::p[1]"
review_emp_name = "xpath://label[text()='Employer:']/following::p[1]"

review_edit_button = "xpath://h2[text()='$$']/following::button[1]"
# Job status
# Financial details
# RESP beneficiary details

beneficiary_details_in_review = "xpath:(//label[normalize-space(text())='$$'])[2]/following::p[1]"
# Name:
# Date of birth:
# Social Insurance Number:

# ------------------------------------------------------------------------------------------
# Conform it's you page
with_photo_id = "xpath://div[@id='div-option-radio-label']"
with_photo_id_agree = "xpath://input[@id='ao_terms_label']"

verify_in_person = "xpath://div[@id='id-physical-radio-label']"
#next btn

# ------------------------------------------------------------------------------------------

# Agreements and disclosures
agreement_page = "xpath://span[text()='Read the agreements and disclosures.']"
term_and_condition = "xpath://input[@id='ao_terms_label']"

# nextbtn

# ------------------------------------------------------------------------------------------

#Choose your signing options
e_sign = "xpath://input[@id='esign-online']"
print_and_sign = "xpath://input[@id='esign-physical']"

# sign up user ID
default_user_id = "xpath://div[contains(text(),'Default numeric user ID')]/following::span[1]/span[2]"
skip_checkbox = "xpath://input[@id='skip']"
custom_user_id = "xpath://input[@id='user_id']"
sign_on_password = "xpath://input[@id='signon_password']"

re_enter_sign_on_password = "xpath://input[@id='signon_confirm_password']"

use_same_password = "xpath://input[@id='radio-primary-ctrl-yes']"
different_password = "xpath://input[@id='radio-primary-ctrl-no']"

# use different password for trading
new_trading_password = "xpath://input[@id='trading_password']"
re_enter_trading_password = "xpath://input[@id='trading_confirm_password']"

# go_green_go_paperless = "xpath:"
get_my_tax_doc_online = "xpath://input[@id='radio-taxSuppression-yes']"
i_prefer_paper = "xpath://input[@id='radio-taxSuppression-no']"

# register btn
# error then click let go button   Let’s go

# ------------------------------------------------------------------------------------------

# complete application
# open_forms_btn = "" btn
