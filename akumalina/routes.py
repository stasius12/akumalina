from akumalina import app
from flask import render_template, request, url_for
import os
from datetime import datetime, timedelta
from collections import defaultdict

from .file_handling import FileHandler
from .plotting import AudioPlotter, TemperaturePlotter
from .recording import Recorder
from .forms import RecordingParamsForm, TemperaturePlotDateForm
from .models import WaveFile


@app.route('/temperatures/', methods=['GET', 'POST'])
def temperatures():
    # === temperatures ===
    form = TemperaturePlotDateForm(request.form or None)
    if form.validate_on_submit():
        date_from = form.date_from.data
        
    data = FileHandler().read_temperatures_data()
    date_to = datetime.today() 
    date_from = date_to - timedelta(days=7)
    data = list(filter(lambda el: el[0] > date_from and el[0] < date_to, data))
    a = TemperaturePlotter(data).create_plot()
    
    vars = {
        'form': form,
    }
    return render_template('temperatures.html', **vars)

@route('/recording/', methods=['GET', 'POST'])
def recording_view():
    # === recording ===
    wavefile = WaveFile.query.order_by(WaveFile.created_at.desc()).first()
    form = RecordingParamsForm(request.form or None)
    if form.validate_on_submit():
        recorder = Recorder(form.duration.data, form.channel_number.data)
        wavefile = recorder.record()
        audio_plotter = AudioPlotter(wavefile)
        audio_plotter.create_plot()
        
    vars = {
        'form': form,
        'wavefile': wavefile,
    }    
    
    return render_template('main.html', **vars)

@app.route('/croatia')
def croatia():
    days = dict()
    movies = [x for x in os.listdir('akumalina/static/croatia/') if x.endswith('.mp4') and x.startswith('day')]
    for movie in movies:
        day = 'day_%s' % movie.split('_')[1]
        if not day in days:
            days[day] = {
               'name': 'Dzień %s' % day.split('_')[-1],
               'movies': []
            }
        days[day]['movies'].append(movie)
    return render_template('croatia.html', days=days)
