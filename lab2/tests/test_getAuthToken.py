import lab2.loadJson as loadJson
from lab2.Api.Api import Api

class TestGetAuthToken:
    def test_getAuthToken(self):
        api = Api()
        loginPassword = loadJson.load_json('../jsons/admin.json')
        schema = loadJson.load_json('../schemas/AuthResponseSchema.json')
        api.post('auth', loginPassword).checkout(schema=schema)
    