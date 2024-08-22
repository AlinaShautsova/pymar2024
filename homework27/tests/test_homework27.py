"""Test homework 27."""
import pytest
import requests

from homework27.models.user import User


def test_correct_create_user(correct_create_user_data):
    """Test correct create user via correct user data."""
    response = User().create_user(correct_create_user_data)
    assert response.status_code == requests.status_codes.codes.ok


def test_incorrect_create_user(incorrect_create_user_data):
    """Test incorrect create user via incorrect create user data."""
    response = User().create_user(incorrect_create_user_data)
    assert response.status_code == requests.status_codes.codes.bad_request


def test_get_created_user(created_user):
    """Test get created user using correct user id."""
    response = User().get_user(created_user['id'])
    assert response.status_code == requests.status_codes.codes.ok


def test_get_nonexistent_user(nonexistent_user_id):
    """Test get nonexistent user using nonexistent id."""
    response = User().get_user(nonexistent_user_id)
    assert response.status_code == requests.status_codes.codes.not_found


def test_correct_update_user(created_user, correct_update_user_data):
    """Test correct update created user via correct update user data."""
    response = User().update_user(created_user['id'], correct_update_user_data)
    assert response.status_code == requests.status_codes.codes.ok
    for key in correct_update_user_data:
        assert response.json()[key] == correct_update_user_data[key]


def test_incorrect_data_update_user(created_user):
    """Test incorrect update created user via incorrect update user data."""
    response = User().update_user(created_user['id'], {})
    assert response.status_code == requests.status_codes.codes.bad_request


def test_incorrect_id_update_user(nonexistent_user_id,
                                  correct_update_user_data):
    """Test incorrect update nonexistent user via correct update user data."""
    response = User().update_user(nonexistent_user_id,
                                  correct_update_user_data)
    assert response.status_code == requests.status_codes.codes.not_found


@pytest.mark.xfail(reason="Ask teacher about 404 error.")
def test_delete_created_user(created_user):
    """Test delete created user using correct user id."""
    response = User().delete_user(created_user['id'])
    assert response.status_code == requests.status_codes.codes.no_content


def test_delete_nonexistent_user(nonexistent_user_id):
    """Test delete nonexistent user using nonexistent id."""
    response = User().delete_user(nonexistent_user_id)
    assert response.status_code == requests.status_codes.codes.not_found
