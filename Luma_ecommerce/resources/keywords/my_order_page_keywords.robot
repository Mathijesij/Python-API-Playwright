*** Settings ***
Library     SeleniumLibrary
Library    String
Resource    common_keywords.robot
Variables   ../../data/input.py

*** Keywords ***
Navigate to user account
    Wait Until Element Is Visible    ${nav_to_dropdown}     ${max_time}
    Click Element    ${nav_to_dropdown}
    Wait Until Element Is Visible    ${my_account}  ${max_time}
    Click Element    ${my_account}

Navigate to my order
    Wait Until Element Is Enabled    ${my_order}    ${max_time}
    Click Element    ${my_order}

Get the order id to verify
    ${verify_order_id}  Get Text    ${get_order_id}
    Set Global Variable    ${verify_order_id}
    
Verify the order id 
    IF    '${verify_order_id}' == '${getting_order_id}'
        Log    Order id is verified. And the Order placed successfully.
    ELSE
         Log    The order does not placed.
    END
    
View the order in my orders
    ${view_order}=      Replace String      ${view_order_td}    dynamic_order_id   ${verify_order_id}
    Wait Until Element Is Visible    ${view_order}    ${max_time}
    Click Element    ${view_order}
    Element Should Contain    //h1/span    Order # ${getting_order_id}