import lab2.loadJson as loadJson
from lab2.Api.Api import Api
import pytest
import json

class TestGetBookingById:
    def load_valid_data():
        with open('../jsons/validCreate.json', 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
        
    def load_invalid_data():
        with open('../jsons/invalidCreate.json', 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
        
    @pytest.mark.parametrize("invalidBooking", load_invalid_data())    
    def test_invalidGetBookingById(self, invalidBooking):
        api = Api()
        api.post('booking',invalidBooking).checkout(predictedCode = 500)
        
    @pytest.mark.parametrize("bookingValid", load_valid_data())    
    def test_getBookingById(self, bookingValid):
        api = Api()
        bookingId = api.post('booking',bookingValid).response.json()['bookingid']
        schema = loadJson.load_json('../schemas/GetBookingResponseSchema.json')
        api.get(f'booking/{bookingId}').checkout(schema=schema, close = False)
        api.delete(f'booking/{bookingId}')
    