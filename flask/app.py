

from flask import Flask
from flask import request
import io
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/', methods=['POST'])
def hello_post():
    print('*'*20)
    print(request.get_data())

if __name__ == '__main__':
    app.run(host='0.0.0.0')