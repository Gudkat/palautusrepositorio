*** Settings ***
Resource        resource.robot

Test Setup      Input New Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    kalle    kalle123
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Create User    kalle    kalle123
    Input Credentials    kalle    123qwerty
    Output Should Contain    Username already taken

Register With Too Short Username And Valid Password
    Input Credentials    ka    kalle123
    Output Should Contain    Username must be at least three letters long and contain only letters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    kalle!    kalle123
    Output Should Contain    Username must be at least three letters long and contain only letters

Register With Valid Username And Too Short Password
    Input Credentials    kalle    ka123
    Output Should Contain    Password must be at least eight symbols long and contain not only letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    kalle    kallekalle
    Output Should Contain    Password must be at least eight symbols long and contain not only letters
