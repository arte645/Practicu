import lab2.loadJson as loadJson
from lab2.Api.Api import Api

def test_getBookingById():
    api = Api()
    schema = loadJson.load_json('schemas/GetBookingResponseSchema.json')
    api.get('booking/1')
    api.checkout(schema=schema)
    