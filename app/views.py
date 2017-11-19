from app import app
from flask import render_template
import yaml

f = open('data.yaml','r')
data = yaml.load(f)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/show')
def show():
    servers = data.keys()


    return render_template('show_info.html',data = data, servers = servers)