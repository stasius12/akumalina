from flask import Flask, render_template
#from flask_caching import Cache
import os
import time
from subprocess import check_output

from file_handling import FileHandler
from plotting import Plotter

app = Flask(__name__)
#cache = Cache(app,config={'CACHE_TYPE': 'simple'})

@app.route('/')
def hello():
    data = FileHandler().read_temperatures_data()
    a = Plotter(data)
    a.create_plot()
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
