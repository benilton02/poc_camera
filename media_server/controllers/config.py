

class MediaServerConfig:
    
    MEDIA_SERVER_PORT = '5001'


class DeviceConnectionConfig:

    DEVICE_SERVER_PORT = '5002'
    DEVICE_SERVER_URL = 'http://192.168.0.41' + ':' + DEVICE_SERVER_PORT
    DEVICE_ACTIVATE_STREAMING_ROUTE = DEVICE_SERVER_URL + 'add'
    DEVICE_ACVIVATE_PAIRING_ROUTE = DEVICE_SERVER_URL + 'add'
    DEVICE_START_CAMERA = DEVICE_SERVER_URL + '/start_camera'
    DEVICE_STOP_CAMERA = DEVICE_SERVER_URL + '/stop_camera'
    DEVICE_STATUS_CAMERA = DEVICE_SERVER_URL + '/status_camera'

    
