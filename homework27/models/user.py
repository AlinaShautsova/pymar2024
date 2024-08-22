"""Module for User API model."""
from homework27.constants import CREATE_USER_URL, GET_USER_URL, \
    UPDATE_USER_URL, DELETE_USER_URL
from homework27.models.base import Base


class User(Base):
    """Class contains User API functionality."""
    def create_user(self, create_params):
        """Create new user via create_params."""
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "email": {"type": "string"},
                "age": {"type": "number"},
                "phoneNumber": {"type": "string"},
                "address": {"type": "string"},
                "role": {"type": "string"},
                "referralCode": {"type": "string"},
                "status": {"type": "string"}
            },
            "required": ["id", "name", "email", "age", "phoneNumber",
                         "address", "role", "referralCode", "status"]
        }
        response = self.send_api_request('post', CREATE_USER_URL,
                                         schema, create_params)
        return response

    def get_user(self, user_id):
        """Get user by user_id."""
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "email": {"type": "string"},
                "age": {"type": "number"},
                "phoneNumber": {"type": "string"},
                "address": {"type": "string"},
                "role": {"type": "string"},
                "referralCode": {"type": "string"},
                "createdAt": {"type": "string"},
                "createdBy": {"type": "string"}
            },
            "required": ["id", "name", "email", "age", "phoneNumber",
                         "address", "role", "referralCode", "createdAt",
                         "createdBy"]
        }
        response = self.send_api_request('get', GET_USER_URL + user_id,
                                         schema)
        return response

    def update_user(self, user_id, update_params):
        """Update user by used_id via update_params."""
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "email": {"type": "string"},
                "age": {"type": "number"},
                "phoneNumber": {"type": "string"},
                "address": {"type": "string"},
                "role": {"type": "string"},
                "referralCode": {"type": "string"},
                "status": {"type": "string"}
            },
            "required": ["id", "name", "email", "age", "phoneNumber",
                         "address", "role", "referralCode", "status"]
        }
        response = self.send_api_request('put', UPDATE_USER_URL + user_id,
                                         schema, update_params)
        return response

    def delete_user(self, user_id):
        """Delete user by user_id."""
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "status": {"type": "string"}
            },
            "required": ["id", "status"]
        }
        response = self.send_api_request('delete', DELETE_USER_URL + user_id,
                                         schema)
        return response
