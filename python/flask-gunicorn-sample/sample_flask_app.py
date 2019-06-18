from flask import Flask, render_template, request, jsonify
import json
import time
from concurrent.futures import ThreadPoolExecutor

from werkzeug.contrib.profiler import ProfilerMiddleware
# from app import app
app = Flask(__name__, template_folder="templates")
import os
deployment_env = os.environ["DEPLOYMENT_ENV"]
# app.config['PROFILE'] = True
# app.wsgi_app = ProfilerMiddleware(app.wsgi_app, sort_by=('tottime','time') ,restrictions=[30])
"""
ncalls: number of times this function was called.
tottime: total time spent inside this function.
percall: this is tottime divided by ncalls.
cumtime: total time spent inside this function and any functions called from it.
percall: cumtime divided by ncalls.
filename:lineno(function): the function name and location.
"""
# https://docs.python.org/3/library/profile.html#pstats.Stats.sort_stats
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-debugging-testing-and-profiling

def mysleep3(n):
    time.sleep(3)
    return n

def mysleep5(n):
    time.sleep(5)
    return n

@app.route('/hello')
def hello_world():
    print("deployment_env", deployment_env)
    return 'Hello, World!'

@app.route('/parallel')
def call_parallel():
    print("Called Parallel")
    executor = ThreadPoolExecutor(max_workers=2)
    a = executor.submit(mysleep3, 30)
    b = executor.submit(mysleep5, 50)
    d = a.result(timeout=10) + b.result(timeout=10)
    print(d)
    executor.shutdown()
    return str(d)

@app.route('/sequence')
def call_sequence():
    print("Called Sequence")
    c = mysleep5(5) + mysleep3(3)
    print(c)
    return str(c)

@app.route('/')
def ui():
    return render_template("index.html")


@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        return jsonify({"status": "success"})
    elif request.method == 'GET':
        params = request.args
        print(params)
        resp_data = [{"header1": "value11", "header2": "value12"},
                {"header1": "value21", "header2": "value22"},
                {"header1": "value31", "header2": "value32"}]
        return jsonify(results=resp_data)


@app.route('/params', methods=['GET'])
def get_params():
    params = {"param11": ["param21", "param22", "param23"], "param12": ["param24", "param25", "param26"]}
    return jsonify(params)


if __name__ == "__main__":
    app.run(debug=True)


"""
Prereqs:
pip3 install flask gunicorn
Run python sample_flask_app.py to run it in flask.
Run gunicorn sample_flask_app:app -c gunicorn_sample_conf.ini.py -e DEPLOYMENT_ENV=DEV to run it in gunicorn 
"""
