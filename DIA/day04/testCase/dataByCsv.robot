*** Settings ***
Library     SeleniumLibrary
Library     BuiltIn

*** Variables ***
${data_file}    C:/Users/MathijesiJohnbritto/PycharmProjects/demo/DIA/day04/data/data.csv
#${data_}    ../data/data.csv
${url}      https://magento.softwaretestingboard.com
${browser}  chrome

# for create an account
${create_account}     (//a[text()='Create an Account'])[1]
${first_name}     id=firstname
${last_name}   id=lastname
${email}        id=email_address
${password}     id=password
${confirm_password}     id=password-confirmation
${create_an_account_btn}    //button/span[text()='Create an Account']
${success_message}      Thank you for registering with Main Website Store.

*** Keywords ***
Launch Browser
    Open Browser    ${url}  ${browser}
    Maximize Browser Window

Read CSV Data
    ${data}=    Evaluate    [line.strip().split(",") for line in open("${data_file}")][1:]
    RETURN    ${data}

Create Account
    [Arguments]     ${fname}   ${lname}    ${mail}   ${pass1}    ${pass2}
    Wait Until Element Is Visible    ${create_account}
    Click Element    ${create_account}
    Input Text    ${first_name}    ${fname}
    Input Text    ${last_name}    ${lname}
    Input Text    ${email}    ${mail}
    Input Text    ${password}    ${pass1}
    Input Text    ${confirm_password}    ${pass2}
    Click Element    ${create_an_account_btn}
    Wait Until Page Contains    ${success_message}      30s
    Page Should Contain    ${success_message}
    
*** Test Cases ***
Create account by using csv file
    ${rows}=    Read CSV Data
         FOR    ${row}    IN    @{rows}
             Launch Browser
             Create Account    ${row}[0]    ${row}[1]    ${row}[2]    ${row}[3]    ${row}[4]
             Close Browser
         END