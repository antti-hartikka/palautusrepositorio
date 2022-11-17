*** Settings ***
Resource  resource.robot
Test Setup  New User Registration

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  antti  antti123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle122
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  an  s4l4s4n4
    Output Should Contain  Username should be at least 3 lowercase letters

Register With Valid Username And Too Short Password
    Input Credentials  antti  s4l4s4n
    Output Should Contain  Password too short or consists of only letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  antti  salasana
    Output Should Contain  Password too short or consists of only letters

*** Keywords ***
New User Registration
    Input New User Command