*** Settings ***
Library     Browser
Resource    variables.robot

*** Keywords ***
Open the browser
    New Browser    ${browser}    headless=false
    Set Browser Timeout    30 seconds
    New Page       ${url}

Verify current page url
    [Arguments]     ${page_url}
    ${current_url}  Get Url
    Should Contain    ${current_url}    ${page_url}

Navigate to signup page
    Click        ${signup_or_login}
    Verify current page url    login

Enter signup details
    [Arguments]     ${user_name}    ${user_email}
    Fill Text    ${name}    ${user_name}
    Fill Text    ${email}    ${user_email}
    Click        ${signup_btn}
    Verify current page url    signup

Enter user infomation
    [Arguments]     ${user_password}    ${day}  ${month}    ${year}     ${f_name}   ${l_name}   ${user_address}     ${user_country}     ${user_state}   ${user_city}    ${user_zipcode}     ${user_mobile_number}
    Click    ${title}
    Fill Text    ${password}    ${user_password}
    Select Options By    ${dob_days}    value   ${day}
    Select Options By    ${dob_month}    text   ${month}
    Select Options By    ${dob_year}    value   ${year}
    Fill Text    ${first_name}    ${f_name}
    Fill Text    ${last_name}    ${l_name}
    Fill Text    ${address}    ${user_address}
    Select Options By    ${country}    value    ${user_country}
    Fill Text    ${state}    ${user_state}
    Fill Text    ${city}    ${user_city}
    Fill Text    ${zipcode}    ${user_zipcode}
    Fill Text    ${mobile_number}    ${user_mobile_number}
    Click    ${create_account_btn}
    Verify that account created successfully

Verify that account created successfully
    Verify current page url    account_created
    Click    ${continue_btn}
    Wait For Elements State    ${account_created_successfully}    visible
    
Delete the account
    Click    ${delete_account}
    Verify current page url    delete_account
    Click    ${continue_btn}
    Wait For Elements State    ${signup_or_login}       visible
