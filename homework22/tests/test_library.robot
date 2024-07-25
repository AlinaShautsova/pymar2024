*** Settings ***
Documentation    Unittest for Homework 11: library.

Library    ../resources/library_keywords.py

*** Variables ***
${BOOK1_TITLE}        Harry Potter
${BOOK1_AUTHOR}       Joanne Rowling
${BOOK1_PAGES}        500
${BOOK1_ISBN}         932-994-555
${BOOK2_TITLE}        Dune
${BOOK2_AUTHOR}       Frank Herbert
${BOOK2_PAGES}        400
${BOOK2_ISBN}         56454-6775
${USER1_NAME}         Kate
${USER2_NAME}         Ira

*** Test Cases ***
Test Book Initialization
    [Documentation]    Testing book initialization.
    ${book} =    Create Book    ${BOOK1_TITLE}    ${BOOK1_AUTHOR}    ${BOOK1_PAGES}    ${BOOK1_ISBN}
    Log    Book details: ${book}
    Should Be Equal    ${book.title}    ${BOOK1_TITLE}
    Should Be Equal    ${book.author}   ${BOOK1_AUTHOR}
    Should Be Equal    ${book.number_of_pages}    ${BOOK1_PAGES}
    Should Be Equal    ${book.isbn}    ${BOOK1_ISBN}
    Should Be Equal    ${book.reserved_by}    ${EMPTY}
    Should Be Equal    ${book.took_by}    ${EMPTY}

Test Get Details
    [Documentation]    Testing getting detailed information about a book.
    ${book} =    Create Book    ${BOOK1_TITLE}    ${BOOK1_AUTHOR}    ${BOOK1_PAGES}    ${BOOK1_ISBN}
    ${details} =    Get Book Details    ${book}
    Log    Book details: ${details}
    Should Be Equal    ${details}    Title: ${BOOK1_TITLE}, Author: ${BOOK1_AUTHOR}, Pages: ${BOOK1_PAGES}, ISBN: ${BOOK1_ISBN}

Test Book Reservation
    [Documentation]    Testing book reservation.
    ${book} =    Create Book    ${BOOK1_TITLE}    ${BOOK1_AUTHOR}    ${BOOK1_PAGES}    ${BOOK1_ISBN}
    ${user1} =    Create User    ${USER1_NAME}
    Reserve Book    ${user1}    ${book}
    ${is_reserved} =    Is Book Reserved    ${book}
    Log    Book reserved: ${is_reserved}
    Should Be True    ${is_reserved}

Test Secondary Book Reservation
    [Documentation]    Testing secondary book reservation.
    ${book} =    Create Book    ${BOOK1_TITLE}    ${BOOK1_AUTHOR}    ${BOOK1_PAGES}    ${BOOK1_ISBN}
    ${user1} =    Create User    ${USER1_NAME}
    ${user2} =    Create User    ${USER2_NAME}
    Reserve Book    ${user1}    ${book}
    Reserve Book    ${user2}    ${book}
    ${reserved_by} =    Book Reserved By    ${book}
    Log    Book reserved by: ${reserved_by}
    Should Be Equal    ${reserved_by}    ${USER1_NAME}

Test Book Taking
    [Documentation]    Testing book taking.
    ${book} =    Create Book    ${BOOK1_TITLE}    ${BOOK1_AUTHOR}    ${BOOK1_PAGES}    ${BOOK1_ISBN}
    ${user1} =    Create User    ${USER1_NAME}
    Take Book    ${user1}    ${book}
    ${is_taken} =    Is Book Taken    ${book}
    Log    Book taken: ${is_taken}
    Should Be True    ${is_taken}

Test Secondary Book Taking
    [Documentation]    Testing secondary book taking.
    ${book} =    Create Book    ${BOOK1_TITLE}    ${BOOK1_AUTHOR}    ${BOOK1_PAGES}    ${BOOK1_ISBN}
    ${user1} =    Create User    ${USER1_NAME}
    ${user2} =    Create User    ${USER2_NAME}
    Take Book    ${user1}    ${book}
    Take Book    ${user2}    ${book}
    ${took_by} =    Book Took By    ${book}
    Log    Book took by: ${took_by}
    Should Be Equal    ${took_by}    ${USER1_NAME}

Test Return Book
    [Documentation]    Testing returning a book.
    ${book} =    Create Book    ${BOOK1_TITLE}    ${BOOK1_AUTHOR}    ${BOOK1_PAGES}    ${BOOK1_ISBN}
    ${user1} =    Create User    ${USER1_NAME}
    Take Book    ${user1}    ${book}
    Return Book    ${user1}    ${book}
    ${took_by} =    Book Took By    ${book}
    Log    Book took by after returning: ${took_by}
    Should Be Empty    ${took_by}

Test Return Book Not Taken
    [Documentation]    Testing returning a book that hasn't been taken.
    ${book} =    Create Book    ${BOOK1_TITLE}    ${BOOK1_AUTHOR}    ${BOOK1_PAGES}    ${BOOK1_ISBN}
    ${user1} =    Create User    ${USER1_NAME}
    ${user2} =    Create User    ${USER2_NAME}
    Take Book    ${user1}    ${book}
    Return Book    ${user2}    ${book}
    ${took_by} =    Book Took By    ${book}
    Log    Book took by after trying to return: ${took_by}
    Should Be Equal    ${took_by}    ${USER1_NAME}
