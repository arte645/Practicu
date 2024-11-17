import json

def load_json(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
