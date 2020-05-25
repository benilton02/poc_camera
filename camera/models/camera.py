from controllers.config import CameraConfig
from multiprocessing import Process
import cv2


class Camera:

    instance_camera = None

    def __new__(cls):
        if cls.instance_camera is None:
            cls.instance_camera = object.__new__(cls)
        return cls.instance_camera

    def __init__(self):
        self.start_thread = ""
        self.camera = cv2.VideoCapture(0)

    def start_camera_thread(self):
        self.CameraConfigStatus = CameraConfig()
        self.camera_status = self.CameraConfigStatus.CAMERA_STATUS
        process = Process(target = self.camera_module)
        process.start()
        return self

    def camera_module(self):
        while self.camera_status == 'ENABLED':
            ret, frame = self.camera.read()
            cv2.imshow('POC camera IP', frame)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break
            self.camera_status = self.CameraConfigStatus.CAMERA_STATUS
        self.camera.release()
        cv2.destroyAllWindows()
        return self
        
