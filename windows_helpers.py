import win32com.client
from ReaderHelpers.connection_json_reader import ConnectionStringsJson
from tuya_api_client import TuyaAPIClient

class WindowsHelpers:
    def __init__(self) :
        self.__target_device_instance = ConnectionStringsJson().get_usb_instance_ID()
        self.__tuya_api_client = TuyaAPIClient()

    def _matches_target_device(self,device_id):
        if device_id == self.__target_device_instance:
            return True
        return False
    
    def on_device_change_event(self, event_type, device_id):
        if event_type == 2:
            if self._matches_target_device(device_id):
                print(f"USB device connected: {device_id}")
                self.__tuya_api_client.set_device_preset()

        elif event_type == 3:
            if self._matches_target_device(device_id):
                print(f"USB device disconnected: {device_id}")
                self.__tuya_api_client.clear_device_presets()

    def listen_for_usb_events(self):
        wmi = win32com.client.GetObject("winmgmts:")
        watcher = wmi.ExecNotificationQuery(
            "SELECT * FROM __InstanceOperationEvent WITHIN 2 "
            "WHERE TargetInstance ISA 'Win32_PnPEntity'"
        )

        # Process each event notification
        while True:
            event = watcher.NextEvent()
            device_id = event.TargetInstance.DeviceID
            event_type = event.Path_.Class

            if "InstanceCreationEvent" in event_type:
                self.on_device_change_event(2, device_id)
            elif "InstanceDeletionEvent" in event_type:
                self.on_device_change_event(3, device_id)
