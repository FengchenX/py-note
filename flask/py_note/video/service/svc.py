from flask import Flask
from  py_service.service import svc

app = svc.app

@app.route('/video')
def video():
    return "video"