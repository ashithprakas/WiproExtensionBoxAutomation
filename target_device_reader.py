import json

class TargetDeviceReader:

    def get_instance_from_config(self):
        with open('TargetDevice.json', 'r') as file:
            data = json.load(file)
    
        return data["INSTANCE_DEVICE_ID"]
