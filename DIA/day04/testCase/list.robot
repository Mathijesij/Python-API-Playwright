*** Settings ***
Library     Collections

*** Test Cases ***
Create a List in RF
    #Create List
    ${list}     Create List     Mark    Smith     Jessie
    Log    Created List: ${list}

    #Append values
    Append To List    ${list}   David   Adam
    Log    Append list: ${list}

    # get value by index
    ${get_value}=    Get From List      ${list}     3
    Log    In index 3: ${get_value}

    # get index by value
    ${get_index}=   Get Index From List    ${list}    Jessie
    Log    Index: ${get_index}

    # get Length
    ${list_length}=     Get Length    ${list}
    Log    Length of the list: ${list_length}

    Should Contain    ${list}    Jessie

    List Should Contain Value    ${list}    Adam

    # remove value
    Remove Values From List    ${list}      David
    Log    After Removed: ${list}

Create Nested List
    ${l1}   Create List     1    2    2    3
    ${l2}   Create List     ${l1}   3   4   5
    Log    Nested List: ${l2}

Combine Sort Slice
    # combine list
    ${list1}    Create List     4   5   4   6   8
    ${list2}    Create List     5   6   7   8   0
    ${l1_l2}=    Combine Lists   ${list1}   ${list2}
    Log    Combined List: ${l1_l2}

    # sorted
    Sort List     ${list1}
    Log    Sorted List: ${list1}

    # slice
    ${slice}=   Get Slice From List    ${list1}     1   4   
    Log    Sliced: ${slice}
    
    