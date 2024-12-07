import lab2.loadJson as loadJson
from lab2.Api.Api import Api

class TestGetBookingById:
    def test_getBookingById(self):
        api = Api()
        booking = loadJson.load_json('../jsons/booking.json')
        bookingId = api.post('booking',booking).response.json()['bookingid']
        schema = loadJson.load_json('../schemas/GetBookingResponseSchema.json')
        api.get(f'booking/{bookingId}').checkout(schema=schema)
    