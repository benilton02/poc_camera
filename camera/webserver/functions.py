from flask import Flask
from controllers.config import CameraConfig
from models.camera import Camera

app = Flask(__name__)
CameraConfigStatus = CameraConfig()
camera_module = Camera()

@app.route("/")
def index():
    return 'Camera server is up, the devoly trinity was here'

@app.route("/start_camera")
def start_camera():
    try:
        CameraConfigStatus.CAMERA_STATUS = "ENABLED"
        camera_module.start_camera_thread()
        response = {"response":"ENABLED"}
        
    except:
        CameraConfigStatus.CAMERA_STATUS = "DISABLED"
        response = {"response":"ERROR"}

    finally:
        return response

@app.route("/stop_camera")
def stop_camera():
    try:
        CameraConfigStatus.CAMERA_STATUS = "DISABLED"
        response = {"response":"DISABLED"}
    
    except:
        response = {"response":"ERROR"}

    finally: 
        return response

@app.route('/test_integration')
def test_integration():
    print('Hello Devs!!!')
    return "It Works !!!"
