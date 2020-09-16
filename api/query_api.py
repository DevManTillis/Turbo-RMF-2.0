#!/usr/bin/env python3
# Reference Endpoints
# /api/auth/register
# /api/auth/login
# Get access token response
# {"refresh": "", "access": ""}

# To get an access token
# 1. navigate UI to http://127.0.0.1:8000/api/login
# 2. copy access token
# 3. paste access token as string in "token" variable
# 4. proceed with requests

import requests

class ApiPythonIntegration():
    def __init__(self, endpoint, token=None):
        self.endpoint = endpoint
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}
    
    def request(self, data=None):
        data = data or {"ip": "1.1.2.3"}
        print(requests.get(self.endpoint, data=data, headers=self.headers).json())

api = ApiPythonIntegration(
        endpoint="http://127.0.0.1:8000/api/v1",
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwMjE3MjYzLCJqdGkiOiJiZjU0NGUzNDA0MDM0OWY1OWNkMjI4ODg2YTk2MTBlMyIsInVzZXJfaWQiOjF9.fNZZnwslspv_MNQxBWtMMsWNXtgopMeIIq5UY8xPN4A")

api.request()
