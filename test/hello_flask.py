#这是一个简单的web
# 这里的信息是从git写入的
#sss
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route('/hello/<name>')
def hello(name):
    print(name)
    print(name)
    return render_template('index.html', name=name)

app.run()

