import controllers.config as config
from multiprocessing import Process
import threading
import cv2



class Camera:


    instance_camera = None
    def __new__(cls):
        if cls.instance_camera is None:
            cls.instance_camera = object.__new__(cls)
            print(cls.instance_camera, "---> Singleton Camera")
        return cls.instance_camera


    # _instance= None

    # @staticmethod
    # def get_instance():
    #     if(Camera._instance == None):
    #         Camera._instance = Camera()
    #     return Camera._instance


    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        instance = config.CameraConfig.get_instance()
        self.instance_camera = None
        self.camera_status = None

    def set_camera_state(self, state_value):
        self.camera_status = state_value

    def get_camera_state(self):
        return self.camera_status

    def start_camera_thread(self):
        pass
        #self.CameraConfigStatus = CameraConfig()
        #print(self.CameraConfigStatus, "---> Config instanciado no camera.py")
        #self.camera_status = self.CameraConfigStatus.CAMERA_STATUS
        # process = Process(target = self.camera_module)
        # process.start()
        # print("\nfuncionou\n")
        # process = threading.Thread(target = self.camera_module)
        # process.start()

    def camera_module(self):
        pass
        # a = 0
        #camera_status = config.CameraConfig.get_status()
        #print("\ncamera_status = {}\n".format(camera_status))
        # while True:
            # a = a+1
            # print(self.get_camera_state(), a)
        #     #camera_status = config.CameraConfig.get_status()
        #     #a = a+1
        #     #print(camera_status, a)
        #     '''
        #     if self.camera_status == 'ENABLED':
        #         print(self.camera_status, a)
        #     elif self.camera_status == 'DISABLED':
        #         print("\n\n\n",self.camera_status,"\n\n\n")
        #         break
        #     '''
        #     '''
        #     ret, frame = self.camera.read()
        #     cv2.imshow('POC camera IP', frame)
        #     if cv2.waitKey(0) & 0xFF == ord('q'):
        #         break
        #     self.camera_status = self.CameraConfigStatus.CAMERA_STATUS
        # self.camera.release()
        # cv2.destroyAllWindows()
        # '''
