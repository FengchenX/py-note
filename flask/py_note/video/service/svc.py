# from flask import Flask
from service import base
from flask import request, json, jsonify

app = base.app


@app.route('/videos')
def video():
    return "video"

@app.route('/videos', methods=['POST'])
def addVideo():
    print(request.get_data())
    return jsonify({"name":"name", "age":10})