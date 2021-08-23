import json
import os


def load_filters():
    with open(os.path.dirname(__file__) + '/../config.json', 'r') as config:
        return json.load(config)['filters']
