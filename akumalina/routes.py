from akumalina import app
from flask import render_template, request, url_for
import os
from datetime import datetime, timedelta
from collections import defaultdict

from .file_handling import FileHandler
from .plotting import AudioPlotter
from .recording import Recorder
from .forms import RecordingParamsForm
from .models import WaveFile


@app.route('/', methods=['GET', 'POST'])
def hello():
    # === temperatures ===
    data = FileHandler().read_temperatures_data()
    date_to = datetime.today() 
    date_from = date_to - timedelta(hours=1)
    data = list(filter(lambda el: el[0] > date_from and el[0] < date_to, data))
    # a = Plotter(data).create_plot()

    # === recording ===
    form = RecordingParamsForm(request.form or None)
    wavefile = WaveFile.query.order_by(WaveFile.created_at.desc()).first()
    if form.validate_on_submit():
        recorder = Recorder(form.duration.data, form.channel_number.data)
        wavefile = recorder.record()
        audio_plotter = AudioPlotter('akumalina/%s' % wavefile.wave_file_path)
        audio_plotter.create_plot()
        
    vars = {
        'form': form,
        'wavefile': wavefile.wave_file_path,
    }    
    
    return render_template('main.html', **vars)

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
