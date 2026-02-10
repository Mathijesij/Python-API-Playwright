*** Settings ***
Library     SeleniumLibrary
Resource    ../page_object/methods/common_keyword.robot

*** Test Cases ***
Sign In to the application
    Launch Browser
    Sign In    ward12234@gmail.com    Ward@123
    Close Browser