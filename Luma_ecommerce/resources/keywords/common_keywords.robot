*** Settings ***
Library     SeleniumLibrary
Variables   ../../data/input.py
Resource    create_account_page_keywords.robot
Resource    sign_in_page_keyword.robot
Resource    luma_homepage_keywords.robot
Resource    select_product_and_add_to_cart.robot
Resource    order_product.robot
Resource    my_order_page_keywords.robot
Resource    ../pageObject/locators/common_locators.robot

*** Keywords ***
Launching Browser
    Open Browser    ${url}  ${browser}
    Maximize Browser Window

