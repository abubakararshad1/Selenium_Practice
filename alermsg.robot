*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Handle Simple Alert
    Open Browser    https://testpages.herokuapp.com/styled/alerts/alert-test.html    Chrome
    Maximize Browser Window
    Set Selenium Speed    .3s

    # Ensure the button is visible before clicking
    Wait Until Element Is Visible    xpath=//input[@id='alertexamples']    timeout=5s
    Click Button    xpath=//input[@id='alertexamples']

    # Wait for the alert and capture its text
    ${alert_text}=    Handle Alert
    Log To Console    Alert message is: ${alert_text}

    Close Browser
