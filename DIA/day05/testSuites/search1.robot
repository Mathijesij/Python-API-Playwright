*** Settings ***
Library     SeleniumLibrary
Resource    ../../day05/resources/keywords/homepage_keywords.robot
Test Setup    Launch Browser
Test Teardown      Close the Browser

*** Test Cases ***
Verify user is able to search bus
    [Tags]  bus
    Enter the source
    Enter the destination
    Click search button