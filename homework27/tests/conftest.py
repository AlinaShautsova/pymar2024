"""Fixtures for API endpoints."""
import random
import string

import pytest
from homework27.constants import USER_NAME, USER_AGE, USER_PHONE_NUMBER, \
    USER_ADDRESS, USER_ROLE, USER_REF_CODE, USER_EMAIL, UPDATE_USER_NAME, \
    UPDATE_USER_AGE, UPDATE_USER_PHONE_NUMBER, UPDATE_USER_ADDRESS, \
    UPDATE_USER_ROLE, UPDATE_USER_REF_CODE, NONEXISTENT_USER_ID
from homework27.models.user import User


@pytest.fixture
def correct_create_user_data():
    """Fixture returns correct data to create a new user."""
    return {
        "name": USER_NAME,
        "email": f'{"".join(random.choices(
            string.ascii_lowercase + string.digits, k=10))}{USER_EMAIL}',
        "age": USER_AGE,
        "phoneNumber": USER_PHONE_NUMBER,
        "address": USER_ADDRESS,
        "role": USER_ROLE,
        "referralCode": USER_REF_CODE
    }


@pytest.fixture(scope="session")
def incorrect_create_user_data():
    """Fixture returns incorrect data for create new user."""
    return {
        "name": "12",
        "email": "test",
        "age": 12,
        "phoneNumber": "12",
        "address": "12",
    }


@pytest.fixture
def created_user(correct_create_user_data):
    """Fixture returns json with created user data."""
    response = User().create_user(correct_create_user_data)
    return response.json()


@pytest.fixture
def correct_update_user_data():
    """Fixture returns correct user data to update user."""
    return {
        "name": UPDATE_USER_NAME,
        "email": f'{"".join(random.choices(
            string.ascii_lowercase + string.digits, k=10))}{USER_EMAIL}',
        "age": UPDATE_USER_AGE,
        "phoneNumber": UPDATE_USER_PHONE_NUMBER,
        "address": UPDATE_USER_ADDRESS,
        "role": UPDATE_USER_ROLE,
        "referralCode": UPDATE_USER_REF_CODE
    }


@pytest.fixture
def nonexistent_user_id():
    """Fixture returns nonexistent user id."""
    return NONEXISTENT_USER_ID
