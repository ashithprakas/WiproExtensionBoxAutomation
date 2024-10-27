import json

class ConfigurationJson:
    def __init__(self):
        with open('configurations.json', 'r') as file:
            self._data = json.load(file)

    def get_preset_commands(self):
        selectedPreset = self._data['SelectedPreset'];
        return self._data[selectedPreset]

    def get_default_commands(self):
        return self._data['Default']
