*** Settings ***
Library     SeleniumLibrary
Resource    common_keywords.robot

*** Keywords ***
Click user's cart
    Wait Until Element Is Visible    ${cart_logo}   ${max_time}
    Click Element    ${cart_logo}
    Wait Until Element Is Visible    ${proceed_to_checkout}     ${max_time}
    Click Element    ${proceed_to_checkout}

Enter shipping address
    [Arguments]     ${street_0}     ${street_1}     ${street_2}     ${enter_city}   ${zip_code}     ${phone}
    Wait Until Element Is Visible    ${saved_address_1}     ${max_time}
    Input Text    ${saved_address_0}    ${street_0}
    Input Text    ${saved_address_1}    ${street_1}
    Input Text    ${saved_address_2}    ${street_2}
    Input Text    ${city}    ${enter_city}
    Click Element    ${state}
    Wait Until Element Is Enabled    ${state_option}    ${max_time}
    Click Element    ${state_option}
    Wait Until Element Is Visible    ${post_code}   ${max_time}
    Input Text    ${post_code}    ${zip_code}
    Input Text    ${telephone}    ${phone}

Navigate to place order
    Wait Until Element Is Visible    ${fixed}   ${max_time}
    Wait Until Element Is Enabled    ${fixed}   ${max_time}
    Click Element    ${fixed}
    Click Element    ${next_btn}

Place the order
    Wait Until Element Is Not Visible    ${page_loader}     ${max_time}
    Wait Until Element Is Enabled    ${display_address}   ${max_time}
    Wait Until Element Is Visible    ${place_order}     ${max_time}
    Wait Until Element Is Not Visible    ${page_loader}     ${max_time}
    Scroll Element Into View    ${place_order}
    Wait Until Element Is Enabled    ${place_order}     ${max_time}
    Click Element    ${place_order}
    Wait Until Element Contains    ${thank_you_message}    ${thank_you_msg}     ${max_time}
    
Get the order id
    ${getting_order_id}     Get Text    ${order_id}
    Set Global Variable    ${getting_order_id}

