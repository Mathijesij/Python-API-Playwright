*** Settings ***
Library     SeleniumLibrary
Resource    ../page_object/methods/keyword.robot

*** Test Cases ***
Sign In to the application
    Launch Browser
    Sign In for error handle
    Close Browser