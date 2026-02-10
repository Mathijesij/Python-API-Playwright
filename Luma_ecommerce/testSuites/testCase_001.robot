*** Settings ***
Library     SeleniumLibrary
Resource    ../resources/keywords/common_keywords.robot
Test Setup  Launching Browser
Test Teardown   Close Browser

*** Test Cases ***
Create a new user and placed an order
    Create account    Jessica     Johaan     jess54ica.johan@gmail.com    Jessica@23Jo    Jessica@23Jo
    Mouse over to women
    select shopping option
    Add the product to cart
    Click user's cart
    Enter shipping address    1849 Maplewood Drive    Apt 12C    Brookdale    California    90234    (555) 628-1937
    Navigate to place order
    Place the order
    Get the order id
    Navigate to user account
    Navigate to my order
    Get the order id to verify
    Verify the order id
    View the order in my orders

Sign in to the account and placed an order
    Sign In    jessica.carter@gmail.com    Jessica@0967
    Mouse over to women
    select shopping option
    Add the product to cart
    Click user's cart
    Navigate to place order
    Place the order
    Get the order id
    Navigate to user account
    Navigate to my order
    Get the order id to verify
    Verify the order id
    View the order in my orders