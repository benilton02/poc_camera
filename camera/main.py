import subprocess
import threading
from webserver.TestCamera import TestCamera
import cv2

def start_camera():
    subprocess.run("uwsgi wsgi.ini", shell = True)
    pass

if __name__ == "__main__":
    start_thread = threading.Thread(target = start_camera)
    start_thread.start()

    test_camera = TestCamera()

    while True:
    
        command = input("1 = Start Camera, 2 = Stop Camera, 3 = Camera Status\n")

        if command == "1":
            test_camera.start_thread()
        else:
            pass
