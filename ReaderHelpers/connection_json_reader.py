import json

class ConnectionStringsJson:
    def __init__(self):
        with open('connectionStrings.json', 'r') as file:
            self._data = json.load(file)

    def get_usb_instance_ID(self):
        return self._data["USB_DEVICE_INSTANCE_ID"]
    
    def get_control_device_ID(self):
        return self._data["CONTROL_DEVICE_ID"]
    
    def get_api_access_ID(self):
        return self._data["ACCESS_ID"]
    
    def get_api_access_KEY(self):
        return self._data["ACCESS_KEY"]
    
    def get_username(self):
        return self._data['USERNAME']
    
    def get_password(self):
        return self._data['PASSWORD']
