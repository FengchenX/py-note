# from flask import Flask
from service import base

app = base.app


@app.route('/video')
def video():
    return "video"