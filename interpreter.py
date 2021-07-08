from flask import Flask, Response
from flask.helpers import url_for
from flask_cors import CORS
from flask import render_template
from flask import request
from playsound import playsound
app = Flask(__name__, static_folder='templates/static')

app.config['ENV'] = 'development'
app.config['DEBUG'] = True

hostName = '192.168.1.199' # Set to ip address or domain, CANNOT BE 0.0.0.0
port = 8109 # Set port to bind to

CORS(app)

def a(file):
    playsound(file)

app.jinja_env.globals.update(port=port)
app.jinja_env.globals.update(hostName=hostName)

@app.route('/ping/', methods = ['GET', 'POST'])
def page(name=None):
    if request.method == 'GET':
        return render_template('index.html', name=name)
    elif request.method == 'POST':
        data = request.form.get('ping')
        if data == 'proposed':
            a('fx.wav')
            return Response("{'status':'success'}", status=200, mimetype='application/json')
        else:
            print('i')
            return Response("{'status':'notfound'}", status=404, mimetype='application/json')

if __name__ == '__main__':
    app.run(host=hostName, port=port)