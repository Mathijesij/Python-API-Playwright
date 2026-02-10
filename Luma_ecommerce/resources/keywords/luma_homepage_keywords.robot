*** Settings ***
Library     SeleniumLibrary
Resource    common_keywords.robot
Variables   ../../data/input.py

*** Keywords ***
Move the cursor into women
    Wait Until Element Is Visible    ${women}   ${max_time}
    Mouse Over    ${women}
    Wait Until Element Is Visible    ${top}     ${max_time}
    Mouse Over    ${top}
    Wait Until Element Is Visible    ${hoodies}     ${max_time}
    Mouse Over    ${hoodies}
    Wait Until Element Is Enabled    ${hoodies}     ${max_time}
    Click Element    ${hoodies}
    Wait Until Element Contains    //h1[@class='page-title']    Hoodies & Sweatshirts

Mouse over to women
    TRY
         Move the cursor into women
    EXCEPT
        Reload Page
        Move the cursor into women
    END
