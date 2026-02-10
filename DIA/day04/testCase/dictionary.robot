*** Settings ***
Library     Collections

*** Test Cases ***
Dictionary
    # create
    ${dic}=     Create Dictionary   name=Jessie     age=23      gender=female
    Log    Created List: ${dic}

    #add value in dictionary
    Set To Dictionary    ${dic}     qulification=MCA    place=chennai
    Log    Add value: ${dic}

    # get value by key
    ${get}=   Get From Dictionary    ${dic}    qulification
    Log    Get value from dic: ${get}

    # get items from dictionary
    ${get_items}=   Get Dictionary Items    ${dic}
    Log    Get all Items: ${get_items}

    # get all keys from dictionary
    ${get_keys}=    Get Dictionary Keys    ${dic}
    Log    Get all Keys: ${get_keys}

    # get all values from dictionary
    ${get_values}=  Get Dictionary Values    ${dic}
    Log    Get all values: ${get_values}

    # pop the paticular one pair from dictionary
    Pop From Dictionary    ${dic}    qulification
    Log    After Popped: ${dic}

    # remove two or more pair from dictionary
    Remove From Dictionary    ${dic}    age     place
    Log    After Remove values: ${dic}
    
    # convert list to dictionary
    @{list1}   Create List  1    2
    @{list2}    Create List     3   4
    @{list3}    Create List     ${list1}    ${list2}
    Log    Before convert: ${list3}
    ${list_to_dic}=    Convert To Dictionary   ${list3}
    Log    After convert: ${list_to_dic}
    
Create Nested Dictionary
    ${dic1}=    Create Dictionary   1=one   2=two
    ${dic2}=    Create Dictionary   3=three     4=four
    ${dic3}=    Create Dictionary   5=five      6=six
    ${dic}=     Create Dictionary   
    Set To Dictionary    ${dic}     &{dic1}
    Set To Dictionary    ${dic}     &{dic2}
    Set To Dictionary    ${dic}     &{dic3}
    Log    Nested Dictionary: ${dic}