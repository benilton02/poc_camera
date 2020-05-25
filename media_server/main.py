from camera_commands.start_stop_camera import *
import subprocess
#import threading
from multiprocessing import Process

def start_server():
    subprocess.run("uwsgi wsgi.ini", shell = True)
    return self

if __name__ == "__main__":
    # start_thread = threading.Thread(target = start_server)
    # start_thread.start()

    process = Process(target = start_server)
    process.start()

    while True:
    
        command = input("1 = Start Camera, 2 = Stop Camera, 3 = Camera Status\n")

        if command == "1":
            start_camera()

        elif command == "2":
            stop_camera()

        elif command == "3":
            status_camera()

        else:
            print("Wrong command")
            continue
