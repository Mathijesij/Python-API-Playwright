*** Settings ***
Library     Browser
Resource    keywords.robot
Test Setup  Open the browser
Test Teardown   Close Browser

*** Test Cases ***
Login to an account
    Navigate to signup page
    Enter signup details    Steve    steve4u32@gmail.com
    Enter user infomation    0987654321    21    January    1997    Steve    Harrington    F-270 George St N    India    ONTARIO    Peterborough    K9J 3H1    9876543457
    Delete the account



