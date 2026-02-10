*** Settings ***
Library     SeleniumLibrary
Resource    common_keywords.robot
Variables   ../../data/input.py

*** Keywords ***
Create an account
    [Arguments]     ${f_name}   ${l_name}   ${mail}    ${pass}     ${confirmpass}
    Wait Until Element Is Visible    ${create_account}  ${max_time}
    Click Element    ${create_account}
    Input Text    ${first_name}    ${f_name}
    Input Text    ${last_name}    ${l_name}
    Input Text    ${email}    ${mail}
    Input Text    ${password}    ${pass}
    Input Text    ${confirm_password}    ${confirmpass}
    Click Element    ${create_an_account_btn}
    Wait Until Element Is Visible    ${success_message}     ${max_time}

Create account
    [Arguments]     ${name1}    ${name2}    ${mail1}    ${pass1}    ${pass2}
    TRY
        Create an account    ${name1}    ${name2}    ${mail1}    ${pass1}    ${pass2}
    EXCEPT
        Reload Page
        Create an account    ${name1}    ${name2}    ${mail1}    ${pass1}    ${pass2}
    END