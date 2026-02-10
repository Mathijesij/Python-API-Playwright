*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}      chrome
${Uname}        //input[@placeholder='Username']
${pwd}          //input[@placeholder='Password']
${sButton}      //button[@type='submit']

*** Keywords ***
Open the HRM
    Wait Until Element Is Visible    ${Uname}
    Element Should Be Visible    ${Uname}
    Input Text    ${Uname}    adminn
    Sleep    3s
#    ${text}=        Get Value         ${Uname}
#    ${length}=      Get Length        ${text}
#    WHILE    ${length} > 0
#        Press Keys    ${Uname}    BACKSPACE
#        ${length}=    Set Variable    ${length - 1}
#    END
    Press Keys    ${Uname}    CONTROL+a    DELETE
    Sleep    3s
    Input Text      ${Uname}    Admin
    Sleep    3s

*** Test Cases ***
Login in HRM
    Open Browser    ${url}      ${browser}
    Open the HRM
    Close Browser
