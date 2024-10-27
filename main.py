import platform
from enum import Enum
from windows_helpers import WindowsHelpers

class OSType(Enum):
    WINDOWS = 1
    LINUX = 2
    MACOS = 3
    OTHER = 4

class App :
    def __init__(self):
       self.__os_type = self._get_os_type()

    def initalize_listeners(self):
        deviceHelper = None
        if self.__os_type == OSType.WINDOWScls:
            deviceHelper = WindowsHelpers()
            deviceHelper.listen_for_usb_events()
        elif self.__os_type == OSType.LINUX:
            pass
            #implement device helper for linux
        elif self.__os_type == OSType.MACOS:
            pass
            #implement device helper for macos
        else :
            raise RuntimeError('OS Not supported')


    def _get_os_type(self):
        sys_type = platform.system()

        if sys_type == "Windows":
            print("Operating System: Windows")
            return OSType.WINDOWS
            
        elif sys_type == "Linux":
            print("Operating System: Linux")
            return OSType.LINUX
            
        elif sys_type == "Darwin":
            print("Operating System: macOS")
            return OSType.MACOS
        else:
            print("Operating System:", sys_type)
            return OSType.OTHER

if __name__ == "__main__":
    app = App()
    try:
        app.initalize_listeners()
    except Exception as exec:
        print('Error occured',exec)