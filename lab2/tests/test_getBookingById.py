import lab2.loadJson as loadJson
from lab2.Api.Api import Api

class TestGetBookingById:
    def test_getBookingById(self):
        api = Api()
        schema = loadJson.load_json('../schemas/GetBookingResponseSchema.json')
        api.get('booking/1').checkout(schema=schema)
    