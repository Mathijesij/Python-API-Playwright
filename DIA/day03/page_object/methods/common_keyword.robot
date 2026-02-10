*** Settings ***
Library     SeleniumLibrary
Resource    ../../page_object/locators/variables.robot

*** Keywords ***
Launch Browser
    Open Browser    ${url}  ${browser}
    Maximize Browser Window

Sign In
    [Arguments]     ${enter_email}      ${enter_password}
    Wait Until Page Contains    Home Page
    Click Element    ${sign_in}
    Wait Until Page Contains    Registered Customers
    Input Text    ${valid_email}    ${enter_email}
    Input Text    ${valid_pass}    ${enter_password}
    Click Element    ${sign_in_btn}