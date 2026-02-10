*** Settings ***
Library     SeleniumLibrary
Test Setup    Launch Browser
Test Teardown      Close Browser

*** variables ***
${url}      https://magento.softwaretestingboard.com
${browser}  chrome

# for create an account
${create_account}     (//a[text()='Create an Account'])[1]
${first_name}     id=firstname
${firstname1}    Harry
${last_name}   id=lastname
${lastname1}     Potter
${email}        id=email_address
${email_address}    harrypotter323@gmail.com
${password}     id=password
${entered_password}     Potter@1323
${confirm_password}     id=password-confirmation
${entered_confirm_password}     Potter@123
${create_an_account_btn}    //button/span[text()='Create an Account']

# for login to the account
${sign_in}      (//a[contains(text(),'Sign In')])[1]
${valid_email}      id=email
${enter_email}      ward12234@gmail.com
${valid_pass}       id=pass
${enter_password}   Ward@123
${sign_in_btn}      (//span[text()='Sign In'])[1]

*** Keywords ***
Launch Browser
    Open Browser    ${url}  ${browser}
    Maximize Browser Window

Create account
    Click Element    ${create_account}
    Input Text    ${first_name}    ${firstname1}
    Input Text    ${last_name}    ${lastname1}
    Input Text    ${email}    ${email_address}
    Input Text    ${password}    ${entered_password}
    Input Text    ${confirm_password}    ${entered_confirm_password}
    Click Element    ${create_an_account_btn}

Sign In
    Click Element    ${sign_in}
    Input Text    ${valid_email}    ${enter_email}
    Input Text    ${valid_pass}    ${enter_password}
    Click Element    ${sign_in_btn}

*** Test Cases ***
Create an Account
    [Documentation]     For creating an account
    Create account

#Sign In to the Account
#    [Documentation]     For Sign in to the account
#    Sign In
