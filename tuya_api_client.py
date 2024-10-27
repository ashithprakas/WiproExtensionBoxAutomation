from tuya_iot import TuyaOpenAPI
from requests import get
from config_json_reader import ConfigJsonReader

# openapi = TuyaOpenAPI(ENPOINT,ACCESS_ID,ACCESS_KEY)

# print(openapi.connect(USERNAME,PASSWORD,'91','smartlife'))
# commands = {
#     'commands':[]
# }

# print(openapi.get(f"/v1.0/iot-03/devices/{DEVICE_ID}/specification"))

class TuyaAPIClient:
    def __init__(self) -> None:
        self._endpoint = "https://openapi.tuyain.com"
        self.__connectionData = ConfigJsonReader()
        self.openApi = TuyaOpenAPI(self._endpoint,self.__connectionData.get_api_access_ID(),self.__connectionData.get_api_access_KEY())
        print('password is of type',self.__connectionData.get_password())
        self.openApi.connect(self.__connectionData.get_username(),self.__connectionData.get_password(),'91','smartlife')

    def get_device_properties(self):
        response = self.openApi.get(f"/v2.0/cloud/thing/{self.__connectionData.get_control_device_ID()}/shadow/properties")
        for property in response['result']["properties"]:
            print('code is : ',property['code'],'Name is : ',property["custom_name"])