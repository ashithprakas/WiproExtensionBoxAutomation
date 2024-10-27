import platform
from enum import Enum
from windows_helpers import WindowsHelpers
import tempfile
import logging
import os

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
        if self.__os_type == OSType.WINDOWS:
            logging.info("Operating System: Windows")
            deviceHelper = WindowsHelpers()
            deviceHelper.listen_for_usb_events()
        elif self.__os_type == OSType.LINUX:
            logging.error(msg='OS Not Supported')
            exit()
            #implement device helper for linux
        elif self.__os_type == OSType.MACOS:
            logging.error(msg='OS Not Supported')
            exit()
            #implement device helper for macos
        else :
            logging.error(msg='OS Not Supported')


    def _get_os_type(self):
        sys_type = platform.system()

        if sys_type == "Windows":
            return OSType.WINDOWS
            
        elif sys_type == "Linux":
            return OSType.LINUX
            
        elif sys_type == "Darwin":
            return OSType.MACOS
        else:
            return OSType.OTHER
        
    def create_temp_and_store_processId(self):
        try:
            temp_dir = tempfile.gettempdir()
            sub_dir = "wipro_smart_extenstion_automate.temp"

            new_dir_path = os.path.join(temp_dir,sub_dir)

            os.makedirs(new_dir_path,exist_ok=True)
            pid = os.getpid()
            pid_file_path = os.path.join(new_dir_path,'wipro_smart_extenstion_automate.pid')

            with open(pid_file_path,'w') as file:
                file.write(str(pid))

        except IOError as e:
            exit()

    def setup_logging_config(self):
        log_directory_name = 'logs'
        if not os.path.exists(log_directory_name):
            os.makedirs(log_directory_name)
        log_file_path = os.path.join(log_directory_name,'debug.log')
        logging.basicConfig(filename=log_file_path ,encoding="utf-8",filemode="a",format="{asctime} - {levelname} - {message}",style="{",datefmt="%Y-%m-%d %H:%M",level=logging.DEBUG)

if __name__ == "__main__":
    app = App()
    try:
        app.create_temp_and_store_processId()
        app.setup_logging_config()
        app.initalize_listeners()
    except Exception as exec:
        logging.critical(exc_info=True)