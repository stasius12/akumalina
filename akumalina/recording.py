import os

class Recorder:
	def __init__(self, duration, channel):
		self.duration = duration
		self.channel = channel

	def record(self):
		os.system('arecord -c %s -f wav -d %s > plik.wav' % (
			self.channel, self.duration
		))