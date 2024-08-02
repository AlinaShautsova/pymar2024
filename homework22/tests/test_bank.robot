*** Settings ***
Documentation    Unittest for Homework 11: bank deposit.

Library    ../resources/bank_keywords.py

*** Variables ***
${USER}    Petya
${INITIAL_AMOUNT}    ${100}
${YEARS}             ${2}


*** Test Cases ***
Test Deposit Initialization
    [Documentation]    Testing deposit initialization.
    ${deposit} =    Create Deposit    ${INITIAL_AMOUNT}     ${YEARS}
    ${amount} =    Get Deposit Amount    ${deposit}
    ${term} =    Get Deposit Term    ${deposit}
    ${rate} =    Get Annual Rate    ${deposit}
    Log    Initial deposit amount: ${amount}
    Log    Deposit term: ${term} ${YEARS}
    Log    Annual interest rate: ${rate}%
    Should Be Equal As Numbers    ${amount}    ${INITIAL_AMOUNT}
    Should Be Equal As Numbers    ${term}    ${YEARS}
    Should Be Equal As Numbers    ${rate}    10

Test Final Amount
    [Documentation]    Testing final amount calculation.
    ${deposit} =    Create Deposit    ${INITIAL_AMOUNT}     ${YEARS}
    ${final_amount} =    Final Amount    ${deposit}
    ${expected_amount} =    Evaluate    100 * (1 + 10 / 12 / 100) ** (2 * 12)
    Log    Calculated final amount: ${final_amount}
    Log    Expected final amount: ${expected_amount}
    Should Be Equal As Numbers    ${final_amount}    ${expected_amount}

Test Bank Deposit
    [Documentation]     Testing bank deposit functionality.
    ${bank} =    Create Bank
    ${final_amount} =    Deposit To Bank    ${bank}    ${USER}     ${INITIAL_AMOUNT}     ${YEARS}
    ${user_amount} =    Withdraw    ${bank}    ${USER}
    Log    Final amount in bank: ${final_amount}
    Log    User amount after withdrawal: ${user_amount}
    Should Be Equal As Numbers    ${user_amount}    ${final_amount}

Test Bank Withdraw
    [Documentation]    Testing bank withdrawal functionality.
    ${bank} =    Create Bank
    ${final_amount} =     Deposit To Bank    ${bank}    ${USER}    ${INITIAL_AMOUNT}    ${YEARS}
    ${withdrawn_amount} =    Withdraw    ${bank}    ${USER}
    Log    Withdrawn amount: ${withdrawn_amount}
    Should Be Equal As Numbers    ${withdrawn_amount}    ${final_amount}

Test Withdraw from Nonexistent User
    [Documentation]    Testing withdrawal for a nonexistent user.
    ${bank} =    Create Bank
    ${withdrawn_amount} =    Withdraw    ${bank}    NonexistentUser
    Log    Withdrawn amount for nonexistent user: ${withdrawn_amount}
    Should Be Equal As Numbers    ${withdrawn_amount}    0


Test Deposit Calculation
    [Documentation]    Testing deposit initialization.
    ${bank} =    Create Bank
    ${final_amount}=    Deposit To Bank     ${bank}     ${USER}    ${INITIAL_AMOUNT}    ${YEARS}
    Log    Final amount after deposit: ${final_amount}
    Should Be True    ${final_amount} > ${INITIAL_AMOUNT}
