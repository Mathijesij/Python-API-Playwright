*** Settings ***
Library     SeleniumLibrary
Resource    ../../page_object/locators/variables.robot
Resource    common_keyword.robot

*** Keywords ***
Sign In for error handle
    TRY
        Click Button    ${sign_in}
    EXCEPT
        Sign In     ward12234@gmail.com    Ward@123
    END

Validation
    Click Element    ${sign_in}
    Click Element    ${sign_in_btn}

    ${error1}=      Get Text    ${get_error1}
    ${error2}=      Get Text    ${get_error2}

    IF    '${error1}' == '${error_msg}'
        Log To Console    Email id field is validated
    ELSE
         Log To Console    No error message found
    END

    IF    '${error2}' == '${error_msg}'
        Log To Console    Password field is validated
    ELSE
         Log To Console    No error message found
    END

Get text from the application
    Click Element    ${women}
    ${hoodies}=     Get Text    ${cloth}
    Set Global Variable    ${hoodies}

Search the cloth by get text
    Click Element    ${search}
    Input Text    ${search}    ${hoodies}
    Sleep    4s
    Clear Element Text    ${search}
    Sleep    2s
    Input Text    ${search}    ${hoodies}
    Wait Until Element Is Visible       ${search_cloth}
    Click Element    ${search_cloth}
    Wait Until Page Contains    Search results for: '${cloth_name}'
    Element Should Contain    ${page_title}    Search results for: '${cloth_name}'