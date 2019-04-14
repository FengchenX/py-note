# from flask import Flask
from service import base
from flask import request, json, jsonify
import uuid
from video.db.pg import sysdb
app = base.app
videoDB=None

@app.route('/videos', methods=['GET'])
def getVideos():
    v=json.loads(request.args.get('video'))
    videos = videoDB.GetVideos(v)
    return jsonify({"code":200, "msg":"success", "data":videos})

@app.route('/videos', methods=['POST'])
def addVideo():
    v = json.loads(request.get_data())
    # print('*'*20, v, uuid.uuid4())
    v['id']=str(uuid.uuid4())
    videoDB.AddVideo(v)
    return jsonify({"code": 200, "msg":'success'})