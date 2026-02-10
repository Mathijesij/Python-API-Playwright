*** Settings ***
Library           RequestsLibrary
Library           Collections

*** Variables ***
${BASE_URL}      https://automationexercise.com

*** Test Cases ***
Get All Products List
    Create Session    mysession    ${BASE_URL}
    ${response}=      GET On Session    mysession    /api/productsList
    ${api_code}=      Get From Dictionary    ${response.json()}    responseCode
    Log               API Response Code: ${api_code}
    Should Be Equal As Integers    ${api_code}    ${200}

POST To All Products List
    Create Session    mysession    ${BASE_URL}
    ${response}=      POST On Session    mysession    /api/productsList
    ${api_code}=      Get From Dictionary    ${response.json()}    responseCode
    ${res_message}=   Get From Dictionary    ${response.json()}    message
    Log    ${response.json()}
    Log               API Response Code: ${api_code}
    Log               Response Message: ${res_message}
    Should Be Equal As Integers    ${api_code}    ${405}
    Should Be Equal As Strings    ${res_message}    This request method is not supported.

GET All Brands List
    Create Session    mysession    ${BASE_URL}
    ${response}=      GET On Session    mysession    /api/brandsList
    ${api_code}=      Get From Dictionary    ${response.json()}    responseCode
    Log               API Response Code: ${api_code}
    Should Be Equal As Integers    ${api_code}    ${200}

PUT To All Brands List
    Create Session    mysession    ${BASE_URL}
    ${response}=      PUT On Session    mysession    /api/brandsList
    ${api_code}=      Get From Dictionary    ${response.json()}    responseCode
    ${res_message}=   Get From Dictionary    ${response.json()}    message
    Log               API Response Code: ${api_code}
    Log               Response Message: ${res_message}
    Should Be Equal As Integers    ${api_code}    ${405}
    Should Be Equal As Strings    ${res_message}    This request method is not supported.

POST To Search Product
    Create Session    mysession    ${BASE_URL}
    &{data}=          Create Dictionary    search_product=Jeans
    ${response}=      POST On Session    mysession    /api/searchProduct    data=${data}
    ${api_code}=      Get From Dictionary    ${response.json()}    responseCode
    ${products}=      Get From Dictionary    ${response.json()}    products
    Log               Product List: ${products}
    Log               API Response Code: ${api_code}
    Should Be Equal As Integers    ${api_code}    ${200}

POST To Search Product without search_product parameter
    Create Session    mysession    ${BASE_URL}
    ${response}=      POST On Session    mysession    /api/searchProduct
    ${api_code}=      Get From Dictionary    ${response.json()}    responseCode
    ${res_message}=   Get From Dictionary    ${response.json()}    message
    Log               API Response Code: ${api_code}
    Log               Response Message: ${res_message}
    Should Be Equal As Integers    ${api_code}    ${400}
    Should Be Equal As Strings    ${res_message}    Bad request, search_product parameter is missing in POST request.

POST To Verify Login with valid details
    Create Session    mysession    ${BASE_URL}
    &{data}=          Create Dictionary    email=jessie24@gmail.com    password=Jessie@23456
    ${response}=      POST On Session    mysession    /api/verifyLogin    data=${data}
    ${status}=        Set Variable    ${response.status_code}
    Log               HTTP Status Code: ${status}
    Should Be Equal As Integers    ${status}    ${200}
    ${json}=          Set Variable    ${response.json()}
    ${code}=          Get From Dictionary    ${json}    responseCode
    ${message}=       Get From Dictionary    ${json}    message
    Log               API Response Code: ${code}
    Log               Message: ${message}
    Should Be Equal As Integers    ${code}    ${200}
    Should Be Equal    ${message}    User exists!

POST To Verify Login without email parameter
    Create Session    mysession    ${BASE_URL}
    &{data}=          Create Dictionary        password=Jessie@23456
    ${response}=      POST On Session    mysession    /api/verifyLogin    data=${data}
    ${api_code}=      Get From Dictionary    ${response.json()}    responseCode
    ${api_message}=   Get From Dictionary    ${response.json()}    message
    Log               API Response Code: ${api_code}
    Should Be Equal As Integers    ${api_code}    ${400}
    Should Be Equal As Strings    ${api_message}    Bad request, email or password parameter is missing in POST request.

DELETE To Verify Login
    Create Session    mysession    ${BASE_URL}
    ${response}=      DELETE On Session    mysession    /api/verifyLogin
    ${api_code}=      Get From Dictionary    ${response.json()}    responseCode
    ${api_message}=   Get From Dictionary    ${response.json()}    message
    Log               API Response Code: ${api_code}
    Should Be Equal As Integers    ${api_code}    ${405}
    Should Be Equal As Strings    ${api_message}    This request method is not supported.

POST To Verify Login with invalid details
    Create Session    mysession    ${BASE_URL}
    &{data}=          Create Dictionary    email=jessie2456555@gmail.com    password=Jessie@2553456
    ${response}=      POST On Session    mysession    /api/verifyLogin    data=${data}
    ${status}=        Set Variable    ${response.status_code}
    Log               HTTP Status Code: ${status}
    Should Be Equal As Integers    ${status}    ${200}
    ${json}=          Set Variable    ${response.json()}
    ${code}=          Get From Dictionary    ${json}    responseCode
    ${message}=       Get From Dictionary    ${json}    message
    Log               API Response Code: ${code}
    Log               Message: ${message}
    Should Be Equal As Integers    ${code}    ${404}
    Should Be Equal    ${message}    User not found!

POST To Create/Register User Account
    Create Session    mysession    ${BASE_URL}
    &{data}=          Create Dictionary     name=Mark   email=markyt678946@gmail.com      password=Markey@2435    title=Mr    birth_date=5    birth_month=March    birth_year=2001    firstname=Mark      lastname=Jordenn    company=Zoho    address1=23/34,logon    address2=5th cross  country=India   zipcode=600003  state=TamilNadu     city=Chennai    mobile_number=8865566877
    ${response}=      POST On Session    mysession    /api/createAccount    data=${data}
    ${json}=          Set Variable    ${response.json()}
    ${code}=          Get From Dictionary    ${json}    responseCode
    ${message}=       Get From Dictionary    ${json}    message
    Log               API Response Code: ${code}
    Log               Message: ${message}
    Should Be Equal As Integers    ${code}    ${201}
    Should Be Equal    ${message}    User created!

PUT METHOD To Update User Account
    Create Session    mysession    ${BASE_URL}
    &{data}=          Create Dictionary     name=Markjohn   email=markey346@gmail.com      password=Markey@2435    title=Mr    birth_date=8    birth_month=March    birth_year=2004    firstname=Mark      lastname=Jorden    company=Zoho    address1=23/34,logon    address2=5th cross  country=India   zipcode=600003  state=TamilNadu     city=Chennai    mobile_number=8865566877
    ${response}=      PUT On Session    mysession    /api/updateAccount    data=${data}
    ${code}=          Get From Dictionary    ${response.json()}    responseCode
    ${message}=       Get From Dictionary    ${response.json()}    message
    Log               API Response Code: ${code}
    Log               Message: ${message}
    Should Be Equal As Integers    ${code}    ${200}
    Should Be Equal    ${message}    User updated!
    &{params}=        Create Dictionary    email=markey346@gmail.com
    ${response}=      GET On Session    mysession    /api/getUserDetailByEmail    params=${params}
    ${user_details}=  Get From Dictionary    ${response.json()}    user
    Log               User Details:${user_details}

GET user account detail by email
    Create Session    mysession    ${BASE_URL}
    &{params}=        Create Dictionary    email=jessie24@gmail.com
    ${response}=      GET On Session    mysession    /api/getUserDetailByEmail    params=${params}
    ${api_code}=      Get From Dictionary    ${response.json()}    responseCode
    ${user_details}=  Get From Dictionary    ${response.json()}    user
    Log               API Response Code: ${api_code}
    Log               User Details:${user_details}
    Should Be Equal As Integers    ${api_code}    ${200}