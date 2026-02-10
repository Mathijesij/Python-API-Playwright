*** Settings ***
Library           RequestsLibrary

*** Variables ***
${BASE_URL}       https://jsonplaceholder.typicode.com

*** Test Cases ***
Getting a Resource
    [Documentation]    Example of GET request
    Create Session    jsonplaceholder    ${BASE_URL}
    ${response}=      GET On Session    jsonplaceholder    /posts/1
    Should Be Equal As Numbers    ${response.status_code}    200
    Log    ${response.json()}

Creating a Resource
    [Documentation]    Example of POST request
    Create Session    jsonplaceholder    ${BASE_URL}
    ${payload}=       Create Dictionary    title=foo    body=bar    userId=1
    ${response}=      POST On Session    jsonplaceholder    /posts    json=${payload}
    Should Be Equal As Numbers    ${response.status_code}    201
    Log    ${response.json()}

Updating a Resource
    [Documentation]     Example of PUT request
    Create Session    api    ${BASE_URL}
    ${payload}=     Create Dictionary   id=1    title=foo   body=bar    userId=1
    ${response}=    PUT On Session      api     /posts/1    json=${payload}
    Should Be Equal As Numbers    ${response.status_code}    200
    Log    ${response.json()}

Patching a Resource
    [Documentation]     Example of PATCH request
    Create Session    api    ${BASE_URL}
    ${payload}=     Create Dictionary   title=boo   body=world
    ${response}=    PATCH On Session    api     /posts/1    json=${payload}
    Should Be Equal As Numbers    ${response.status_code}    200
    Log    ${response.json()}

POST a resquest
    [Documentation]    Example of POST request
    Create Session    jsonplaceholder    ${BASE_URL}
    ${payload}=       Create Dictionary    title=foo    body=bar    userId=1
    ${response}=      POST On Session    jsonplaceholder    /posts    json=${payload}
    Should Be Equal As Numbers    ${response.status_code}    201
    Log    ${response.json()}

# Updating a Resource    # robotcode: ignore
#     [Documentation]     Example of PUT request
#     Create Session    api    ${BASE_URL}
#     ${payload}=     Create Dictionary   id=1    title=foo   body=bar    userId=1
#     ${response}=    PUT On Session      api     /posts/1    json=${payload}
#     Should Be Equal As Numbers    ${response.status_code}    200
#     Log    ${response.json()}

# Patching a Resource
#     [Documentation]     Example of PATCH request
#     Create Session    api    ${BASE_URL}
#     ${payload}=     Create Dictionary   title=boo   body=world
#     ${response}=    PATCH On Session    api     /posts/1    json=${payload}
#     Should Be Equal As Numbers    ${response.status_code}    200
#     Log    ${response.json()}
