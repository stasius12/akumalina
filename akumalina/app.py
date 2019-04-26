from flask import Flask, render_template
from flask_caching import Cache
import time
from subprocess import check_output

app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

@app.route('/')
@cache.cached(timeout=50)
def hello():
    time.sleep(10)
    check_output('./temperatures/rysowanie.sh')
    return render_template('main.html')

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
