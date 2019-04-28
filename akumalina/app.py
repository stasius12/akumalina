from flask import Flask, render_template
import os
from datetime import datetime, timedelta
from collections import defaultdict

from file_handling import FileHandler
from plotting import Plotter
from recording import Recorder
from forms import RecordingParamsForm

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=('GET', 'POST'))
def hello():
    # === temperatures ===
    data = FileHandler().read_temperatures_data()
    date_to = datetime.today() 
    date_from = date_to - timedelta(hours=1)
    data = list(filter(lambda el: el[0] > date_from and el[0] < date_to, data))
    # a = Plotter(data).create_plot()

    # === recording ===
    form = RecordingParamsForm()
    if form.validate_on_submit():
        recorder = Recorder(5, 1)
        recorder.record()
    
    return render_template('main.html', form=form)

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
