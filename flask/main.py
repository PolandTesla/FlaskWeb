from flask import *
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

my_list = [1,2,3]
@app.route('/')
def index():
    return render_template('home.html', my_list=my_list)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if (request.form['username'] == "TetsUserName" and 
            request.form['password'] == "123_Rrad"):
            pass
        else:
            abort(401)
    return render_template('login.html')

@app.route('/regiatration', methods=['POST', 'GET'])
def regiatration():
    return render_template('regiatration.html')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    custom_sending("test Sending")

def custom_sending(str):
    emit('my response', str)

if __name__ == '__main__':
	socketio.run(app,debug = True)