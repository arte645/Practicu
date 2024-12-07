from playwright.sync_api import sync_playwright
from jsonschema import validate

class Api:
    base_url = 'https://restful-booker.herokuapp.com/'

    def __init__(self):
        self.response = None
        self.launch_browser()
        
    def launch_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch()
        self.context = self.browser.new_context()
        
    def get(self, path: str):  
        self.response = self.context.request.get(f'{self.base_url}{path}')
        return self
    
    def post(self, path: str, json_body: dict = None):        
        self.response = self.context.request.post(f'{self.base_url}{path}', data=json_body)
        return self
    
    def checkout(self, schema, predictedCode = 200):
        assert self.response.status == predictedCode, f'Expected status 200, got {self.response.status}'
        validate(instance=self.response.json(), schema=schema)
        self.close()
        
    def close(self):
        if self.playwright:
            self.playwright.stop() 
