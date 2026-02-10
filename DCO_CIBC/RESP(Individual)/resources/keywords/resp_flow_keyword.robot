*** Settings ***
Library     SeleniumLibrary
Resource    common_keywords.robot
Library     resp_keyword.py
Library    Collections
Variables   ../pageObjects/locators.py
Variables   ../../data/data.py

*** Keywords ***
Choose the account type
    Wait Until Element Is Visible    ${dont_have_acc}     ${time_out}
    Click Element    ${dont_have_acc}

Select the check box
    Wait Until Element Is Visible    ${understand_and_agree_checkbox}   ${time_out}
    Click Element    ${understand_and_agree_checkbox}

Select the type of account
    Wait Until Element Is Visible    ${select_resp}     ${time_out}
    Click Element    ${select_resp}

Select Individual resp
    Wait Until Element Is Visible    ${individual_resp}     ${time_out}
    Click Element    ${individual_resp}

Validate entered mobile number
    [Arguments]     ${validate_mobile_number}
    ${get_mobile_number}    Get Text    ${validate_entered_phone}
    ${validate}=    Validate Mobile Number    ${get_mobile_number}
    Run Keyword    Should Be Equal    ${validate}    ${validate_mobile_number}

Verify the entered address
    [Arguments]     ${validate_address}
    ${get_address}=    Get Text    ${validate_entered_address}
    Should Be Equal As Strings    ${get_address}    ${validate_address}

Verify the DOB
    [Arguments]     ${validate_month}   ${validate_day}     ${validate_year}
    ${list_of_month}=   Create List     January    February    March    April    May    June    July    August    September    October    November    December
    ${validate_month_by_index}  Get Index From List     ${list_of_month}    ${validate_month}
    ${month_as_number}      Evaluate     "{:02}".format(${validate_month_by_index}+1)
    ${get_validate_dob}=    Get Text    ${validate_entered_dob}
    Should Be Equal    ${get_validate_dob}    ${month_as_number}/${validate_day}/${validate_year}

User temporary sin number
    [Arguments]     ${sin_exp_month}    ${sin_exp_day}      ${sin_exp_year}
    Wait Until Element Is Visible    ${sin_expire_month}    ${time_out}
    Click Element    ${sin_expire_month}
    Select value for the exp month    ${sin_exp_month}
    Input Text    ${sin_expire_day}    ${sin_exp_day}
    Input Text    ${sin_expire_year}    ${sin_exp_year}

Enter the beneficiary temporary sin number
    [Arguments]     ${sin_month}     ${sin_day}      ${sin_year}
    Click Element    ${beneficiary_sin_month}
    Select value from a dropdown    ${sin_month}
    Input Text    ${beneficiary_sin_day}    ${sin_day}
    Input Text    ${beneficiary_sin_year}    ${sin_year}

Enter Personal informations
    [Arguments]     ${user_title}   ${first_name_data}    ${last_name_data}     ${dob_month_data}   ${dob_day_data}     ${dob_year_data}    ${sin_data}     ${sin_exp_month}    ${sin_exp_day}  ${sin_exp_year}  ${email_data}      ${mobile_num_data}  ${address_unit}     ${img}
    Wait Until Element Is Visible    ${title}   ${time_out}
    Click Element    ${title}
    Select value from a dropdown    ${user_title}
    Input Text    ${first_name}    ${first_name_data}
    Input Text    ${last_name}    ${last_name_data}
    Click Element    ${dob_month}
    Select value for the dob month    ${dob_month_data}
    Input Text    ${dob_day}    ${dob_day_data}
    Input Text    ${dob_year}    ${dob_year_data}
    Input Text    ${sin}    ${sin_data}
    ${sin_first_number}=    Evaluate    '${sin_data}'[0]
    Run Keyword If    '${sin_first_number}'=='9'    User temporary sin number    ${sin_exp_month}    ${sin_exp_day}      ${sin_exp_year}
    Input Text    ${email_address}    ${email_data}
    Input Text    ${mobile_phone_number}    ${mobile_num_data}
    Select the address by unit    ${address_unit}
    Capture Page Screenshot    ${screenshot_path}personal_information_page_${img}.png
    Click Next Button

Verify the entered personal information
    [Arguments]     ${value1}     ${value2}     ${value3}   ${value4}     ${value5}     ${value6}     ${value7}     ${value8}     ${value9}     ${value10}     ${value11}   ${img}

    Wait Until Element Is Visible    ${validate_entered_name}   ${time_out}

    ${get_validate_enter_name}=     Get Text    ${validate_entered_name}
    Run Keyword     Should Be Equal    ${get_validate_enter_name}    ${value1} ${ran_first_name} ${ran_last_name}
    Log    User's number is verified

    ${get_validate_email}=  Get Text    ${validate_entered_email}
    Run Keyword    Should Be Equal    ${get_validate_email}    ${value2}
    Log    User's Email id is verified

    ${get_validate_sin}=  Get Text    ${validate_entered_sin}
    Run Keyword    Should Be Equal    ${get_validate_sin}    ${value3}
    Log    User's SIN number is verified

    Validate entered mobile number    ${value4}
    Log    User's Mobile number is verified

    Verify the entered address    ${value5}\n${value6}, ${value7}\n${value8}
    Log    User's Address is verified

    Verify the DOB    ${value9}    ${value10}    ${value11}
    Log    User's DOB is verified
    Capture Page Screenshot    ${screenshot_path}verify_personal_details_page_${img}.png
    Click Confirm Button

Taxpayer Information
    [Arguments]     ${click_canadian_citizen}    ${click_resident_of_canada}    ${enter_country_of_citizenship1}     ${enter_country_of_citizenship2}   ${img}
    ${user_given_value1}=   Replace String    ${canadian_citizen}    $$    ${click_canadian_citizen}
    ${user_given_value2}=   Replace String    ${resident_of_canada}    $$    ${click_resident_of_canada}
    Wait Until Element Is Visible    ${user_given_value1}   ${time_out}
    Click Element    ${user_given_value1}
    Run Keyword If    '${click_canadian_citizen}' == 'No'    Select value from a dropdown    ${enter_country_of_citizenship1}
    Click Element    ${user_given_value2}
    Run Keyword If    '${click_resident_of_canada}' == 'No'    Select value from a dropdown    ${enter_country_of_citizenship2}
    Capture Page Screenshot     ${screenshot_path}taxpayer_information_page_${img}.png
    Click Next Button

Enter spouse details if yes
    [Arguments]     ${enter_spouse_title}   ${enter_spouse_first_name}  ${enter_spouse_last_name}   ${enter_spouse_emp_status}  ${img}
    Wait Until Element Is Visible    ${spouse_title}    ${time_out}
    Click Element    ${spouse_title}
    Select value from a dropdown    ${enter_spouse_title}
    Input Text    ${spouse_first_name}    ${enter_spouse_first_name}
    Input Text    ${spouse_last_name}    ${enter_spouse_last_name}
    Click Element    ${spouse_employment_status}
    Select value from a dropdown    ${enter_spouse_emp_status}
    Capture Page Screenshot     ${screenshot_path}spouse_information_page_${img}.png
    Click Next Button

Enter the value in Employment Status
    [Arguments]     ${emp_status}   ${emp_type_of_business}     ${emp_occupation}    ${emp_name}   ${emp_address_unit}  ${img}
    Wait Until Element Is Visible    ${employment_status}   ${time_out}
    Click Element    ${employment_status}
    Select value from a dropdown    ${emp_status}
    Wait Until Element Is Visible    ${type_of_business}    ${time_out}
    Click Element    ${type_of_business}
    Select value from a dropdown    ${emp_type_of_business}
    Wait Until Element Is Visible    ${occupation}  ${time_out}
    Click Element    ${occupation}
    Select value from a dropdown    ${emp_occupation}
    Input Text    ${employer_name}    ${emp_name}
    Select the address by unit    ${emp_address_unit}
    Capture Page Screenshot     ${screenshot_path}employement_status_page_${img}.png
    Click Next Button

Enter the financial Details
    [Arguments]     ${liquid_asset}     ${fixed_asset}      ${liabilities}      ${enter_annual_income}  ${source_income}    ${investing_year}   ${img}
    Wait Until Element Is Visible    ${household_liquid_asset}  ${time_out}
    Input Text    ${household_liquid_asset}    ${liquid_asset}
    Input Text    ${household_fixed_asset}    ${fixed_asset}
    Input Text    ${household_liabilities}    ${liabilities}
    
    ${get_total_amount_of_asset}=   Get Text    ${displayed_total_assert}
    ${get_amt_formatted}=    For Get Amount    ${get_total_amount_of_asset}
    ${add_total_amount}=    Add Asset Amount    ${liquid_asset}    ${fixed_asset}
    Run Keyword     Should Be Equal    ${get_amt_formatted}    ${add_total_amount}
    Log    Total assert is verified

    ${get_liabilities}=     Get Text    ${displayed_liabilities}
    ${get_lib_formatted}=   For Get Amount    ${get_liabilities}
    Run Keyword     Should Be Equal    ${liabilities}    ${get_lib_formatted}
    Log    Given Liabilities is verified

    ${get_total_net_worth}=     Get Text    ${displayed_total_net_worth}
    ${get_total_net_worth_formatted}=   For Get Amount    ${get_total_net_worth}
    ${sum_the_total_worth}=     Evaluate    ${add_total_amount}-${get_lib_formatted}
    ${total_worth}=     Convert To String    ${sum_the_total_worth}
    Run Keyword    Should Be Equal    ${total_worth}    ${get_total_net_worth_formatted}
    Log    Net worth is verified

    Input Text    ${annual_income}    ${enter_annual_income}
#    Wait Until Element Is Visible    ${annual_income_source}    ${time_out}
#    Click Element    ${annual_income_source}
#    Select value from a dropdown    ${source_income}

    Wait Until Element Is Visible    ${years_of_investing}  ${time_out}
    Input Text    ${years_of_investing}    ${investing_year}
    Capture Page Screenshot     ${screenshot_path}financial_details_page_${img}.png
    Click Next Button

Select the Bank Information
    [Arguments]     ${img}
    Wait Until Element Is Visible    ${dont_link_a_bank_acc}    ${time_out}
    Click Element    ${dont_link_a_bank_acc}
    Capture Page Screenshot     ${screenshot_path}bank_information_page_${img}.png
    Click Next Button

Select yes or no in trading privileges
    [Arguments]     ${choice}   ${img}
    Wait Until Element Is Visible    ${option_trading_privileges}   ${time_out}
    Select User choice for yes or no    ${choice}
    Capture Page Screenshot     ${screenshot_path}trading_privileges_page_${img}.png
    Click Next Button

Enter Beneficiary information
    [Arguments]     ${spouse}   ${title1}   ${name1}    ${name2}    ${month}    ${day}  ${year}    ${gender}   ${ben_sin}  ${sin_month}     ${sin_day}      ${sin_year}     ${ben_resident}     ${ben_age}   ${img}
    Wait Until Element Is Visible    ${relationship_to_you}     ${time_out}
    Click Element    ${relationship_to_you}
    Select value from a dropdown    ${spouse}
    Click Element    ${beneficiary_title}
    Select value from a dropdown    ${title1}
    Input Text    ${beneficiary_first_name}    ${name1}
    Input Text    ${beneficiary_last_name}    ${name2}
    Click Element    ${beneficiary_dob_month}
    Select value from a dropdown    ${month}
    Input Text    ${beneficiary_dob_day}    ${day}
    Input Text    ${beneficiary_dob_year}    ${year}
    Click Element    ${beneficiary_gender}
    Select value from a dropdown    ${gender}
    Input Text    ${beneficiary_sin}    ${ben_sin}
    ${ben_sin_first_number}=    Evaluate    '${ben_sin}'[0]
    Run Keyword If    '${ben_sin_first_number}'=='9'    Enter the beneficiary temporary sin number    ${sin_month}     ${sin_day}      ${sin_year}
    Beneficiary resident of canada    ${ben_resident}
    Click Element    ${beneficiary_address_same_as_sub}
    Under Age    ${ben_age}
    Capture Page Screenshot     ${screenshot_path}beneficiary_details_page_${img}.png
    Click Next Button

Enter education and funding details
    [Arguments]     ${value1}   ${value2}   ${value3}   ${img}
    Wait Until Element Is Visible    ${cesg_yes}    ${time_out}
    Run Keyword If    '${value1}'=='Yes'    Click Element    ${cesg_yes}
    Run Keyword If    '${value1}'=='No'    Click Element    ${cesg_no}

    Run Keyword If    '${value2}'=='Yes'    Click Element    ${additional_cesg_yes}
    Run Keyword If    '${value2}'=='No'    Click Element    ${additional_cesg_no}

    Run Keyword If    '${value3}'=='Yes'    Click Element    ${canada_learning_bond_yes}
    Run Keyword If    '${value3}'=='No'    Click Element    ${canada_learning_bond_no}

    Capture Page Screenshot     ${screenshot_path}education_and_funding_details_page_${img}.png

    Click Next Button

Select Final question
    [Arguments]     ${value1}   ${value2}   ${value3}   ${value4}   ${value5}   ${value6}   ${value7}   ${value8}   ${img}
    Wait Until Element Is Visible    ${user_alone_or_as_part_of_a_group_hold_yes}   ${time_out}
    Run Keyword If    '${value1}'=='Yes'    Click Element    ${user_alone_or_as_part_of_a_group_hold_yes}
    Run Keyword If    '${value1}'=='No'    Click Element    ${user_alone_or_as_part_of_a_group_hole_no}

    Run Keyword If    '${value2}'=='Yes'    Click Element    ${spouse_alone_or_as_part_of_a_group_hold_yes}
    Run Keyword If    '${value2}'=='No'    Click Element    ${spouse_alone_or_as_part_of_a_group_hole_no}

    Run Keyword If    '${value3}'=='Yes'    Click Element    ${reporting_issue_or_other_issue_yes}
    Run Keyword If    '${value3}'=='No'    Click Element    ${reporting_issue_or_other_issue_no}

    Run Keyword If    '${value4}'=='Yes'    Click Element    ${spouse_reporting_issue_or_other_issue_yes}
    Run Keyword If    '${value4}'=='No'    Click Element    ${spouse_reporting_issue_or_other_issue_no}

    Run Keyword If    '${value5}'=='Yes'    Click Element    ${living_in_same_home_yes}
    Run Keyword If    '${value5}'=='No'    Click Element    ${living_in_same_home_no}

    Run Keyword If    '${value6}'=='Yes'    Click Element    ${spouse_living_in_same_home_yes}
    Run Keyword If    '${value6}'=='No'    Click Element    ${spouse_living_in_same_home_no}

    Run Keyword If    '${value7}'=='Yes'    Click Element    ${i_do_not_object}
    Run Keyword If    '${value7}'=='No'    Click Element    ${i_do_object}

    Run Keyword If    '${value8}'=='No'    Click Element    ${security_holder_material_no}
    Run Keyword If    '${value8}'=='PYes'    Click Element    ${proxy_related_material_yes}
    Run Keyword If    '${value8}'=='FYes'    Click Element    ${security_holder_material_yes}

    Capture Page Screenshot     ${screenshot_path}final_question_page_${img}.png
    Click Next Button

Review Information
    [Arguments]     ${occupation_info}      ${employer_info}    ${img}
    Wait Until Element Is Visible    ${review_occupation}   ${time_out}
    ${get_occuption_info}=  Get Text    ${review_occupation}
    ${get_emp_name}=    Get Text    ${review_emp_name}
    Run Keyword     Should Be Equal    ${occupation_info}    ${get_occuption_info}
    Log    Occupation is verified
    Run Keyword     Should Be Equal    ${employer_info}    ${get_emp_name}
    Log    Occupation is verified
    Capture Page Screenshot     ${screenshot_path}review_information_page_${img}.png
    Click Next Button

Confirm its you
    [Arguments]     ${img}
    Wait Until Element Is Visible    ${verify_in_person}    ${time_out}
    Click Element    ${verify_in_person}
    Capture Page Screenshot     ${screenshot_path}confirm_its_you_page_${img}.png
    Click Next Button

Agreement and Disclosure page
    [Arguments]     ${img}
    Wait Until Element Is Visible    ${agreement_page}     ${time_out}
    Click Element    ${term_and_condition}
    Capture Page Screenshot     ${screenshot_path}agreement_disclosure_page_${img}.png
    Click Next Button

Choose your sign in option
    [Arguments]     ${img}
    Wait Until Element Is Visible    ${print_and_sign}  ${time_out}
    Click Element    ${print_and_sign}
    Capture Page Screenshot     ${screenshot_path}sign_in_page_${img}.png
#    Click Next Button

Create RESP individual account
    ${index}=   Set Variable    1
    ${rows}=    Read CSV Data
    FOR    ${row}    IN    @{rows}
        # open browser
        Open the browser

        # before pass data
        Run Keyword     Select type of an investors edge account    ${index}
        Log    Type of Investors edge is selected and navigated to next page
        Run Keyword     Terms and conditions    ${index}
        Log    Terms and condition is accpected and navigated to next page
        Run Keyword     Select type of account      ${index}
        Log    Account type is selected and navigated to next page

        # process data
        Create RESP by valid details    ${row}  ${index}

        Close Browser
        ${index}=    Evaluate    ${index} + 1
    END

Create RESP by valid details
        [Arguments]     ${row}      ${img}
        # personal infomation
        ${given_title}=     Set Variable    ${row}[0]
        ${ran_first_name}   ${ran_last_name}=   Generate Name By Title    ${given_title}
        ${create_random_sin}=   Generate Valid Sin
        Set Global Variable    ${ran_first_name}
        Set Global Variable     ${ran_last_name}
        Enter Personal informations    ${row}[0]    ${ran_first_name}    ${ran_last_name}    ${row}[3]    ${row}[4]    ${row}[5]    ${create_random_sin}    ${row}[7]    ${row}[8]    ${row}[9]    ${row}[10]    ${row}[11]    ${row}[12]   ${img}

        # verify personal
        Verify the entered personal information    ${row}[0]    ${row}[10]    ${create_random_sin}    ${row}[11]     ${row}[12]    ${row}[13]    ${row}[14]    ${row}[15]    ${row}[3]    ${row}[4]    ${row}[5]    ${img}

        # taxpayer information
        Taxpayer Information    ${row}[16]    ${row}[18]    ${row}[17]  ${row}[19]  ${img}

        # Marital Status
        ${given_title}=     Set Variable    ${row}[21]
        ${spe_first_name}   ${spe_last_name}=   Generate Name By Title    ${given_title}
        Select yes or no    ${row}[20]
        Enter spouse details if yes    ${row}[21]    ${spe_first_name}    ${spe_last_name}    ${row}[22]    ${img}

        # employment status
        ${enter_name_randomly}=     Generate Random Name
        Set Global Variable    ${enter_name_randomly}
        Enter the value in Employment Status    ${row}[23]    ${row}[24]    ${row}[25]    ${enter_name_randomly}    ${row}[26]  ${img}

        # financial details
        Enter the financial Details    ${row}[30]    ${row}[31]    ${row}[32]    ${row}[33]    ${row}[34]    ${row}[35]     ${img}

        # select banking account
        Select the Bank Information     ${img}
        
        #RESP Account
        Select yes or no in trading privileges    ${row}[36]    ${img}

        # Beneficiary information
        ${given_title}=     Set Variable    ${row}[38]
        ${ben_first_name}   ${ben_last_name}=   Generate Name By Title    ${given_title}
        ${random_sin}=  Generate Valid Sin
        Enter Beneficiary information    ${row}[37]    ${row}[38]    ${ben_first_name}    ${ben_last_name}    ${row}[39]    ${row}[40]    ${row}[41]    ${row}[42]    ${random_sin}     ${row}[57]  ${row}[58]  ${row}[59]    ${row}[44]  ${row}[45]   ${img}

        #RESP eduction and funding
        Enter education and funding details    ${row}[46]    ${row}[47]    ${row}[48]   ${img}

        # final question
        Select Final question    ${row}[49]    ${row}[50]    ${row}[51]    ${row}[52]    ${row}[53]    ${row}[54]    ${row}[55]    ${row}[56]   ${img}

        # review information
        Review Information    ${row}[25]    ${enter_name_randomly}      ${img}

        TRY
            Confirm its you     ${img}
            Agreement and Disclosure page   ${img}
        EXCEPT
            Agreement and Disclosure page   ${img}
        END

        # choose the sign in option
        Choose your sign in option      ${img}

Verify the error message in personal information
    Wait Until Element Is Visible    ${title}   ${time_out}
    Click Next Button
    Verify the fields    ${title_error_msg}
    Log    Title field error message verified
    Verify the fields    ${first_name_error_msg}
    Log    First name field error message is verified
    Verify the fields    ${last_name_error_msg}
    Log    Last name field error message is verified
    Verify the fields    ${sin_error_msg}
    Log    sin field error message is verified
    Verify the fields    ${email_error_msg}
    Log    Email field error message is verified
    Verify the fields    ${mobile_error_msg}
    Log    Mobile number field error message is verified
    Verify the fields    ${address_error_msg}
    Log    Address Unit field error message is verified
    Verify the fields    ${city_error_msg}
    Log    City field error message is verified
    Verify the fields    ${province_error_msg}
    Log    Province field error message is verified
    Verify the fields    ${postal_code_error_msg}
    Log    Postal code field error message is verified
    Capture Page Screenshot     ${screenshot_path}verify_the_fields.png


