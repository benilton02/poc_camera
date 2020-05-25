from flask import Flask
import controllers.config as config
from models.camera import Camera

app = Flask(__name__)
#CameraConfigStatus = CameraConfig()
camera_module = Camera()
instance = config.CameraConfig.get_instance()

@app.route("/")
def index():
    return 'Camera server is up, the devoly trinity was here'

@app.route("/start_camera")
def start_camera():
    try:
        #config.CameraConfig.set_status("ENABLED") 
        camera_module.set_camera_state("ENABLED")
        camera_module.start_camera_thread()
        response = {"response":"ENABLED"}
        
    except:
        #config.CameraConfig.set_status("DISABLED")
        camera_module.set_camera_state("DISABLED")
        response = {"response":"ERROR"}

    return response

@app.route("/stop_camera")
def stop_camera():
    try:
        #config.CameraConfig.set_status("DISABLED")
        camera_module.set_camera_state("DISABLED")
        response = {"response":"DISABLED"}
        
    except:
        response = {"response":"ERROR"}

    return response

@app.route("/status_camera")
def status_camera():
    #status = config.CameraConfig.get_status()
    status = camera_module.get_camera_state()
    print(status)
    response = {"response":status}
    return response

@app.route('/test_integration')
def test_integration():
    print('Hello Devs!!!')
    return "It Works !!!"
