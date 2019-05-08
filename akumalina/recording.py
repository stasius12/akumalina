import os
import uuid
from .models import WaveFile
from . import db

class Recorder:
    def __init__(self, duration, channel):
        self.duration = duration
        self.channel = channel

    def record(self):
        os.system('arecord -c %s -t wav -d %s -r 44100 > akumalina/static/%s' % (
            self.channel, self.duration, self.get_unique_filename()
        ))
        wave_file = WaveFile(wave_file_path='static/%s' % self.get_unique_filename())
        db.session.add(wave_file)
        db.session.commit()
        return wave_file
    
    def get_unique_filename(self):
        if not hasattr(self, 'filename'):
            self.filename = str(uuid.uuid4())
        return '%s.wav' % self.filename