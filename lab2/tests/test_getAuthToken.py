import lab2.loadJson as loadJson
from lab2.Api.Api import Api

def test_getAuthToken():
    api = Api()
    loginPassword = loadJson.load_json('../jsons/admin.json')
    schema = loadJson.load_json('../schemas/AuthResponseSchema.json')
    api.post('auth', loginPassword).checkout(schema=schema)
    