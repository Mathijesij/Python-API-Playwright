*** Settings ***
Library     SeleniumLibrary
Resource    ../page_object/methods/keyword.robot

*** Test Cases ***
Verify the validation in sign in page
    Launch Browser
    Validation