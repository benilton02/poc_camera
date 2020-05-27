import threading
import cv2


class TestCamera:

    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.camera.read()
        return frame

    def start_thread(self):
        start_thread_camera = threading.Thread(target = self.show_camera)
        start_thread_camera.start()
        return None
    
    def show_camera(self):
        while True:
            frame = self.get_frame()
            cv2.imshow('POC camera IP', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
