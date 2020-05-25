from camera_commands.start_stop_camera import *
import subprocess
import threading


def start_server():
    subprocess.run("uwsgi wsgi.ini", shell = True)

if __name__ == "__main__":
    start_thread = threading.Thread(target = start_server)
    start_thread.start()

    while True:
    
        command = input("1 = Start Camera, 2 = Stop Camera, 3 = Stop Process")

        if command == "1":
            start_camera()

        elif command == "2":
            stop_camera()

        elif command == "3":
            stop_camera()
            break

        else:
            print("Wrong command")
            continue
