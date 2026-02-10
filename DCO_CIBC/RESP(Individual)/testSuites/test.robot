*** Settings ***
Library     SeleniumLibrary
Resource    ../resources/keywords/common_keywords.robot
#Test Setup    Open the browser
#Test Teardown   Close Browser

*** Test Cases ***
TC001
    [Documentation]     Create a RESP individual account by multiple valid data
    Create RESP individual account

TC002
    [Documentation]     Verify the error message in the personal information fields
    Open the browser
    Select type of an investors edge account    verify1
    Terms and conditions    verify2
    Select type of account    verify3
    Verify the error message in personal information
    Close Browser
