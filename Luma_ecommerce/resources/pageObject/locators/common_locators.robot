*** Settings ***
Resource    sign_in_page_locators.robot
Resource    hoodies_and_sweatshirts_locators.robot
Resource    product_detail_locators.robot
Resource    create_account_page_locators.robot
Resource    luma_homepage_locators.robot
Resource    user_profile_locators.robot
Resource    shipping_address_locators.robot

*** Variables ***
${success_message}      //div[contains(@class,'success message')]
${page_loader}      //div[@class='loader']