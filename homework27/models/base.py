"""Module for Base API model."""
import os

import requests
from jsonschema import validate

from homework27.constants import MAIN_URL


class Base:
    """Class contains base API functionality."""
    def __init__(self):
        """Initialize the object."""
        self.url = MAIN_URL

    def send_api_request(self, method, endpoint, schema, json=None):
        """Send api request and validate response."""
        if json is None:
            json = {}
        headers = {'Authorization': f'Bearer {os.getenv("AUTH_TOKEN")}',
                   'Content-Type': 'application/json'}

        session = requests.Session()
        request = requests.Request(method, self.url + endpoint, json=json,
                                   headers=headers)
        prepared_request = request.prepare()
        response = session.send(prepared_request)
        if str(response.status_code).startswith('2'):
            validate(response.json(), schema)
        return response
