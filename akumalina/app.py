from flask import Flask, render_template
#from flask_caching import Cache
import os
from datetime import datetime, timedelta
from collections import defaultdict
from subprocess import check_output

from file_handling import FileHandler
from plotting import Plotter

app = Flask(__name__)
#cache = Cache(app,config={'CACHE_TYPE': 'simple'})

@app.route('/')
def hello():
    data = FileHandler().read_temperatures_data()
    date_to = datetime.today() 
    date_from = date_to - timedelta(hours=1)
    data = list(filter(lambda el: el[0] > date_from and el[0] < date_to, data))
    print(data)
    a = Plotter(data).create_plot()
    return render_template('main.html')

@app.route('/croatia')
def croatia():
    days = dict()
    movies = [x for x in os.listdir('static/croatia/') if x.endswith('.mp4') and x.startswith('day')]
    for movie in movies:
        day = 'day_%s' % movie.split('_')[1]
        if not day in days:
            days[day] = {
               'name': 'Dzień %s' % day.split('_')[-1],
               'movies': []
            }
        days[day]['movies'].append(movie)
    return render_template('croatia.html', days=days)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
