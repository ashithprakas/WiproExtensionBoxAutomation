import json

class TargetDeviceReader:

    def get_instance_from_config(self):
        # Change the file name to the correct JSON file
        with open('TargetDevice.json', 'r') as file:
            data = json.load(file)
    
        return data["INSTANCE_DEVICE_ID"]
