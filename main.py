# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, jsonify,request

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

########    

@app.route('/')

@app.route('/user/<username>')
def show_user_profile(username):  # http://127.0.0.1:5000/user/RickyS
    # show the user profile for that user
    return 'User %s' % username
@app.route('/hello')
def hello1():         # http://127.0.0.1:5000/hello
    return 'Hello Python'

@app.route('/add/<A>and<B>')
def add(A,B):         # http://127.0.0.1:5000/add/4and5
    num=int(A)+int(B)
    num1=str(num)
    return num1

#########################################################################
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])  # http://127.0.0.1:5000/todo/api/v1.0/tasks
def get_tasks():
    return jsonify({'tasks': tasks})

###############################POST##########################################
    
@app.route('/register', methods=['POST'])   # http://127.0.0.1:5000/register
def register():
    print(request.headers)
    # print(request.stream.read()) # 不要用，否则下面的form取不到数据
    print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='little apple'))
    
    password_num= request.form['password']
    print(password_num)
    print(type(password_num))
    
    password_num1 = int(password_num)+20
    
    return str(password_num1 )



def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown123', methods=['POST'])  # http://127.0.0.1:5000/shutdown
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run()
    
# Crtl+C to stop 
    
    
    
########










if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
