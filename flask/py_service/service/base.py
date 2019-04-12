from flask  import Flask
app = Flask(__name__)

app.config['JSON_AS_ASCII']=False

@app.route('/')
def hello_world():
    return 'Hello World,  My first flask!'


