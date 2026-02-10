*** Settings ***
Library     SeleniumLibrary
Resource    ../page_object/methods/keyword.robot
*** Test Cases ***
Sign In to the application
    Launch Browser
    Get text from the application
    Search the cloth by get text
    Close Browser