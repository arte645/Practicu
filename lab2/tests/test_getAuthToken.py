import lab2.loadJson as loadJson
from lab2.Api.Api import Api
import pytest
import json


class TestGetAuthToken:
    def load_valid_data():
        with open('../jsons/validToken.json', 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
        
    def load_invalid_data():
        with open('../jsons/InvalidToken.json', 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
        
    @pytest.mark.parametrize("loginPasswordValid", load_valid_data())
    def test_getAuthTokenValid(self, loginPasswordValid):
        api = Api()
        schema = loadJson.load_json('../schemas/AuthResponseSchema.json')
        api.post('auth', loginPasswordValid).checkout(schema=schema)
        
    @pytest.mark.parametrize("loginPasswordInvalid", load_invalid_data())
    def test_getAuthTokenInvalid(self, loginPasswordInvalid):
        api = Api()
        schema = loadJson.load_json('../schemas/reason.json')
        api.post('auth', loginPasswordInvalid).checkout(schema=schema)
    