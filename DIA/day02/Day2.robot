*** Settings ***
Library    customs_library.py

*** Keywords ***
Sum Two Numbers
    [Arguments]    ${a}    ${b}
    ${add_number}=    Add Two Number    ${a}    ${b}
    RETURN    ${add_number}

Minus Two Numbers
    [Arguments]     ${c}    ${d}
    ${sub_number}=      Sub Two Number    ${c}    ${d}
    RETURN    ${sub_number}

*** Test Cases ***
Addition
    ${add}=      Sum Two Numbers    20    30
    Log To Console    ${add}

Subtraction
    ${sub}=     Minus Two Numbers    23    12
    Log To Console    ${sub}