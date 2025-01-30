from Computer import *
import json


class DataHandler:
    FILE_NAME = 'data.json'

    @staticmethod
    def load_data():
        try:
            with open(DataHandler.FILE_NAME, 'r') as file:
                data = json.load(file)
                return [Computer.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def save_data(computers):
        with open(DataHandler.FILE_NAME, 'w') as file:
            json.dump([comp.to_dict() for comp in computers], file, indent=4)


