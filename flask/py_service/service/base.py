from flask  import Flask
from conf.settings import Config

app = Flask(__name__)

app.config['JSON_AS_ASCII']=False
app.config.from_object(Config)

@app.route('/')
def hello_world():
    return 'Hello World,  My first flask!'


