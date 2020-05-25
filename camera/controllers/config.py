class CameraConfig:
    
    MEDIA_SERVER_PORT = '5005'
    CAMERA_STATUS = 'DISABLED'
    instance_config = None

    _instance= None

    @staticmethod
    def get_instance():
        if(CameraConfig._instance == None):
            CameraConfig._instance = CameraConfig()
        return CameraConfig._instance

    @staticmethod
    def get_status():
        return CameraConfig.CAMERA_STATUS

    @staticmethod
    def set_status(new_status):
        CameraConfig.CAMERA_STATUS = new_status

    # def __new__(cls):
    #     if cls.instance_config is None:
    #         cls.instance_config = object.__new__(cls)
    #         print( cls.instance_config, "---> Singleton config")
    #     return cls.instance_config

class MediaServerConnectionConfig:

    CAMERA_SERVER_PORT = '5001'
    CAMERA_SERVER_URL = '0.0.0.0'
    CAMERA_ACTIVATE_STREAMING_ROUTE = CAMERA_SERVER_URL + ':' + CAMERA_SERVER_PORT
    CAMERA_ACVIVATE_PAIRING_ROUTE = CAMERA_SERVER_URL + ':' + CAMERA_SERVER_PORT
