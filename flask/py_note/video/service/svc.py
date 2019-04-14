# from flask import Flask
from service import base
from flask import request, json, jsonify
from video.db.pg import sysdb
app = base.app
videoDB=None

@app.route('/videos', methods=['GET'])
def getVideos():
    videos = videoDB.GetVideos()
    print("*"*20, videos)
    return jsonify({"code":200, "msg":"success", "data":videos})

@app.route('/videos', methods=['POST'])
def addVideo():
    videoDB.AddVideo( json.loads(request.get_data()))
    return jsonify({"code": 200, "msg":'success'})