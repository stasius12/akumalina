import matplotlib.pyplot as plt
import scipy.io.wavfile
import numpy as np
import os

from .models import WaveFile

class TemperaturePlotter:
    def __init__(self, data):
        self.data = data
    
    def create_plot(self):
        x_data = [x[0] for x in self.data]
        y_data = [x[1] for x in self.data]
        plt.plot(x_data, y_data)
        plt.gcf().autofmt_xdate()
        plt.savefig('static/test.png')


class AudioPlotter:
    def __init__(self, wave_file):
        self.wave_file = wave_file
        self.path_to_file = 'akumalina/%s' % wave_file.wave_file_path
      
    def get_wave_file(self, fs_=False):
        if not hasattr(self, 'wave'):
            wave_file_path = self.path_to_file
            fs, wave = scipy.io.wavfile.read(wave_file_path)
            self.wave = wave / (np.iinfo(np.uint8).max + 1) - 0.5
            self.fs = fs
        return self.wave, self.fs if fs_ else self.wave    
    
    def create_plot(self):
        wave, fs = self.get_wave_file(True)
        x = np.arange(len(wave))/float(fs)
        plt.plot(x, wave)
        self.save_plot_to_file()

    def save_plot_to_file(self):
        path = WaveFile.get_default_time_plot_path(self.get_unique_filename())
        plt.savefig('akumalina/%s' % path)
        self.wave_file.update_time_plot_path(path)

    def get_unique_filename(self):
        if not hasattr(self, 'filename'):
            self.filename = '%s.png' % str(uuid.uuid4())
        return self.filename
