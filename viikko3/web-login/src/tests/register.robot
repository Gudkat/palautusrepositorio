*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Go To Register Page


*** Test Cases ***
Register With Valid Credentials
    Set Username    kalle
    Set Password    kalle123
    Set Password Confimation    kalle123
    Submit Credentials
    Welcome Should Be Open

Register With Nonmatching Password And Password Confirmation
    Set Username    kalle
    Set Password    kalle123
    Set Password Confimation    kalle1234
    Submit Credentials
    Registration Should Fail With Message    Password and password confirmation do not match

Register With Too Short Username And Valid Password
    Set Username    ka
    Set Password    kalle123
    Set Password Confimation    kalle123
    Submit Credentials
    Registration Should Fail With Message    Username must be at least three letters long and contain only letters

Register With Valid Username And Invalid Password
    Set Username    kalle
    Set Password    kalle
    Set Password Confimation    kalle
    Submit Credentials
    Registration Should Fail With Message    Password must be at least eight symbols long and contain not only letters

*** Keywords ***
Submit Credentials
    Click Button    Register

Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Set Password Confimation
    [Arguments]    ${password}
    Input Password    password_confirmation    ${password}

Registration Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}
