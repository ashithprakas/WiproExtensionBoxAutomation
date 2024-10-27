from tuya_iot import TuyaOpenAPI
from requests import get
from connection_json_reader import ConnectionStringsJson
from configuration_json_reader import ConfigurationJson

class TuyaAPIClient:
    def __init__(self) -> None:
        self._endpoint = "https://openapi.tuyain.com"
        self.__connectionData = ConnectionStringsJson()
        self.__configurations = ConfigurationJson()
        self.openApi = TuyaOpenAPI(self._endpoint,self.__connectionData.get_api_access_ID(),self.__connectionData.get_api_access_KEY())
        self.openApi.connect(self.__connectionData.get_username(),self.__connectionData.get_password(),'91','smartlife')

    def get_device_properties(self):
        response = self.openApi.get(f"/v2.0/cloud/thing/{self.__connectionData.get_control_device_ID()}/shadow/properties")
        for property in response['result']["properties"]:
            print('code is : ',property['code'],'Name is : ',property["custom_name"]);

    def set_device_preset(self):
 
        response = self.openApi.post(f"/v1.0/iot-03/devices/{self.__connectionData.get_control_device_ID()}/commands",self.__configurations.get_preset_commands())
        print(response)

    def clear_device_presets(self):
        response = self.openApi.post(f"/v1.0/iot-03/devices/{self.__connectionData.get_control_device_ID()}/commands",self.__configurations.get_default_commands())