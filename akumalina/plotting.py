import matplotlib.pyplot as plt
import scipy.io.wavfile
import numpy as np
import os

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
    def __init__(self, wave_filename):
        self.wave_filename = wave_filename
      
    def get_wave_file(self, fs_=False):
        if not hasattr(self, 'wave'):
            wave_filename = self.wave_filename
            fs, wave = scipy.io.wavfile.read(wave_filename)
            self.wave = wave / (np.iinfo(np.uint8).max + 1) - 0.5
            self.fs = fs
        return self.wave, self.fs if fs_ else self.wave    
	
    def create_plot(self):
        wave, fs = self.get_wave_file(True)
        x = np.arange(len(wave))/float(fs)
        plt.plot(x, wave)
        self.save_plot_to_file()

    def save_plot_to_file(self):
        strFile = 'akumalina/static/audioplot.png'
        if os.path.isfile(strFile):
            os.remove(strFile)
        plt.savefig(strFile)
