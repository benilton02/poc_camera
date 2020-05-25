from controllers.config import DeviceConnectionConfig
import requests


DeviceConfig = DeviceConnectionConfig()
def start_camera():
    URL = DeviceConfig.DEVICE_START_CAMERA
    set_camera_status = {'camera_status': "ENABLED"}
    request = requests.get(url=URL, params=set_camera_status)
    data = request.json()
    
    if data["response"] == "ENABLED":
        print('\n\nCamera was activated')
    else:
        print('\n\nWasnt possible to activate camera')
    pass

def stop_camera():
    URL = DeviceConfig.DEVICE_STOP_CAMERA
    set_camera_status = {'camera_status': "DISABLED"}
    request = requests.get(url=URL, params=set_camera_status)
    data = request.json()
    
    if data["response"] == "DISABLED":
        print('\n\nCamera was deactivated')
    
    else:
        print('\n\nWasnt possible to deactivate camera')
    pass

def status_camera():
    URL = DeviceConfig.DEVICE_STATUS_CAMERA
    request = requests.get(url=URL)
    print(request)
    pass
