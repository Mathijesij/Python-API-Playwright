*** Settings ***
Library     SeleniumLibrary
Resource    common_keywords.robot
Variables   ../../data/input.py

*** Keywords ***
select shopping option
    Wait Until Element Is Visible    ${style}   ${max_time}
    Click Element    ${style}
    Wait Until Element Is Visible    ${hoodie}  ${max_time}
    Click Element    ${hoodie}
    Wait Until Element Is Visible    ${product_1}   ${max_time}
    Click Element    ${product_1}

Add the product to cart
    Wait Until Element Is Visible    ${size}    ${max_time}
    Click Element    ${size}
    Click Element    ${color}
    Click Element    ${add_to_cart}
    Wait Until Element Is Visible    ${success_message}     ${max_time}



