*** Settings ***
Library     SeleniumLibrary
Resource    common_keywords.robot
Variables   ../../data/input.py

*** Keywords ***
Sign In to the account
    [Arguments]     ${v_mail}   ${v_pass}
    Wait Until Element Is Visible    ${sign_in}     ${max_time}
    Click Element    ${sign_in}
    Input Text    ${valid_email}    ${v_mail}
    Input Text    ${valid_pass}    ${v_pass}
    Click Element    ${sign_in_btn}
    Wait Until Element Is Visible    ${after_sign_in}   ${max_time}

Sign In
    [Arguments]     ${valid_mailid}     ${valid_password}
    TRY
        Sign In to the account      ${valid_mailid}     ${valid_password}
    EXCEPT
        Reload Page
        Sign In to the account      ${valid_mailid}     ${valid_password}
    END