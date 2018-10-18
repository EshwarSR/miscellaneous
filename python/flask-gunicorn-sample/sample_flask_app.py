from flask import Flask
import time
from concurrent.futures import ThreadPoolExecutor

from werkzeug.contrib.profiler import ProfilerMiddleware
# from app import app
app = Flask(__name__)

app.config['PROFILE'] = True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, sort_by=('tottime','time') ,restrictions=[30])
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

if __name__ == "__main__":
    app.run(debug=True)


"""
Prereqs:
pip3 install flask gunicorn
Run python sample_flask_app.py to run it in flask.
Run gunicorn sample_flask_app:app -c gunicorn_sample_conf.ini.py to run it in gunicorn 
"""
