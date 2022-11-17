*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Username is too short or not characters a-z

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Click Button  Register
    Register Should Fail With Message  Password is too short or contains only characters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle12
    Click Button  Register
    Register Should Fail With Message  Password and confirmation does not match

Login After Succesful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Go To Main Page
    Click Button  Logout
    Login Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
   Set Username  kalle
   Set Password  kalle123
   Set Password Confirmation  kalle12
   Click Button  Register
   Go To Login Page
   Login Page Should Be Open
   Set Username  kalle
   Set Password  kalle123
   Submit Credentials
   Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

Register Should Fail With Message
    [Arguments]  ${MESSAGE}
    Register Page Should Be Open
    Page Should Contain  ${MESSAGE}

Set Password Confirmation
    [Arguments]  ${PASSWORD}
    Input Password  password_confirmation  ${PASSWORD}
