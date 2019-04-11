# from flask import Flask
from  py_note.video.service import svc

if __name__ == '__main__':
    svc.app.run(host='0.0.0.0')