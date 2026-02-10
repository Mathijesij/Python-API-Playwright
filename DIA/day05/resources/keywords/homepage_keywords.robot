*** Settings ***
Library     SeleniumLibrary
Resource    ../../resources/pageObject/homepage_locators.robot
Resource    ../../data/data.robot

*** Keywords ***
Launch Browser
    Open Browser    ${url}  ${browser}
    Maximize Browser Window

Close the Browser
    Close Browser

Enter the source
    Wait Until Element Is Visible    ${leave_from}
    Click Element    ${leave_from}
    Input Text    ${leave_from}    ${source_city}
    Wait Until Element Is Visible    ${enter_source}  ${timeout}
    Click Element    ${enter_source}

Enter the destination
    Click Element    ${going_To}
    Input Text    ${going_To}    ${destination_city}
    Wait Until Element Is Visible    ${enter_destination}
    Click Element    ${enter_destination}

Click search button
    Click Element    ${search}
    Wait Until Element Is Visible    ${sort_by}     ${timeout}

Click Today button
    Click Element    ${today}
    Wait Until Element Is Visible    ${sort_by}     ${timeout}

Click Tomorrow button
    Click Element    ${tomorrow}
    Wait Until Element Is Visible    ${sort_by}     ${timeout}

Select Date
    Click Element   ${onward_journey_date}
    Click Element    ${date}