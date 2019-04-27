import matplotlib.pyplot as plt

class Plotter(object):
	def __init__(self, data):
		self.data = data

	def create_plot(self):
		plt.plot([1,2,3], [4,5,6])
		# plt.show()
		# plt.savefig('static/test1.png')