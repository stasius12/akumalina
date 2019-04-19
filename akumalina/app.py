from flask import Flask, render_template
import os
from subprocess import check_output

app = Flask(__name__)

@app.route('/')
def hello():
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
