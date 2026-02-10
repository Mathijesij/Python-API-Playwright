*** Settings ***
Library     SeleniumLibrary
Library    String
Resource    resp_flow_keyword.robot
Variables   ../pageObjects/locators.py

*** Keywords ***
Open the browser
    Open Browser    ${url}  ${browser}
    Maximize Browser Window

Read CSV Data
    ${data}=    Evaluate    [line.strip().split(",") for line in open("${data_file_path}")][1:]
    RETURN    ${data}

Click Accept all cookies button
    ${accept_all_cookies_button}=    Replace String    ${navigation_button}    $$    ${accept_all_cookies_btn}
    Wait Until Element Is Visible    ${accept_all_cookies_button}    ${time_out}
    Click Element    ${accept_all_cookies_button}

Click Start Application Button
    ${start_application_button}=    Replace String    ${navigation_button}    $$    ${start_application_btn}
    Wait Until Element Is Visible    ${start_application_button}    ${time_out}
    Click Element    ${start_application_button}

Click Next Button
    ${next_button}=    Replace String    ${navigation_button}    $$    ${next_btn}
    Wait Until Element Is Visible    ${next_button}    ${time_out}
    Click Element    ${next_button}

Click Back Button
    ${back_button}=    Replace String    ${navigation_button}    $$    ${back_btn}
    Wait Until Element Is Visible    ${back_button}    ${time_out}
    Click Element    ${back_button}

Click Confirm Button
    ${confirm_button}=    Replace String    ${navigation_button}    $$    ${confirm_btn}
    Wait Until Element Is Visible    ${confirm_button}    ${time_out}
    Click Element    ${confirm_button}

Click Edit Button
    ${edit_button}=    Replace String    ${navigation_button}    $$    ${edit_btn}
    Wait Until Element Is Visible    ${edit_button}    ${time_out}
    Click Element    ${edit_button}

Click Lets Go Button
    ${lets_go_button}=      Replace String    ${navigation_button}    $$    ${lets_go_btn}
    Wait Until Element Is Visible    ${lets_go_button}  ${time_out}
    Click Element    ${lets_go_button}

Select value from a dropdown
   [Arguments]  ${select_value}
   ${selected_value}=    Replace String    ${select_object}    $$      ${select_value}
   Wait Until Element Is Visible    ${selected_value}    ${time_out}
   Click Element    ${selected_value}

Select value for the dob month
    [Arguments]     ${selecting_dob_month}
    ${selected_dob_month}=  Replace String    ${select_dob_month}    $$    ${selecting_dob_month}
    Wait Until Element Is Visible    ${selected_dob_month}    ${time_out}
    Click Element    ${selected_dob_month}

Select value for the exp month
    [Arguments]     ${selecting_exp_month}
    ${selected_exp_month}=  Replace String    ${select_exp_month}    $$    ${selecting_exp_month}
    Wait Until Element Is Visible    ${selected_exp_month}    ${time_out}
    Click Element    ${selected_exp_month}

Select the address by unit
    [Arguments]     ${select_address_unit}
    Click Element    ${address_including_unit}
    Input Text    ${address_including_unit}    ${select_address_unit}
    ${selected_address_unit}=       Replace String    ${select_base_on_unit}    $$    ${select_address_unit}
    Wait Until Element Is Visible    ${selected_address_unit}   ${time_out}
    Click Element    ${selected_address_unit}

Verify the fields
    [Arguments]     ${err_message}
    ${error_message}=   Replace String    ${error_message_text}    $$    ${err_message}
    Element Should Contain    ${error_message}    ${err_message}

Select User choice for yes or no
    [Arguments]     ${value}
    Wait Until Element Is Visible    ${yes}     ${time_out}
    Run Keyword If    '${value}' == 'No'  Click Element    ${no}
    Run Keyword If    '${value}' == 'Yes'    Click Element    ${yes}

Select yes or no
    [Arguments]     ${value}
    Wait Until Element Is Visible    ${spouse_common_law_partner_yes}   ${time_out}
    Run Keyword If    '${value}' == 'No'  Click Element    ${spouse_common_law_partner_no}
    Run Keyword If    '${value}' == 'Yes'    Click Element    ${spouse_common_law_partner_yes}

Under Age
    [Arguments]     ${value}
    Wait Until Element Is Visible    ${below_age}   ${time_out}
    Run Keyword If    '${value}' == 'No'  Click Element    ${above_age}
    Run Keyword If    '${value}' == 'Yes'    Click Element    ${below_age}

Beneficiary resident of canada
    [Arguments]     ${value}
    Wait Until Element Is Visible    ${beneficiary_resident_of_canada_yes}   ${time_out}
    Run Keyword If    '${value}' == 'No'  Click Element    ${beneficiary_resident_of_canada_no}
    Run Keyword If    '${value}' == 'Yes'    Click Element    ${beneficiary_resident_of_canada_yes}

# ----------------------------------------------------------------------------------

# to start the application
Select type of an investors edge account
    [Arguments]     ${img}
    Click Accept all cookies button
    Choose the account type
    Capture Page Screenshot     ${screenshot_path}select_investors_ac_${img}.png
    Click Start Application Button

Terms and conditions
    [Arguments]     ${img}
    Select the check box
    Select User choice for yes or no    No
    Capture Page Screenshot     ${screenshot_path}terms_and_condition_${img}.png
    Click Start Application Button

Select type of account
    [Arguments]     ${img}
    Select the type of account
    Select Individual resp
    Capture Page Screenshot     ${screenshot_path}selected_type_ac_${img}.png
    Click Next Button


