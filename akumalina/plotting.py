import matplotlib.pyplot as plt

class Plotter(object):
   def __init__(self, data):
      self.data = data
	
   def create_plot(self):
      x_data = [x[0] for x in self.data]
      y_data = [x[1] for x in self.data]
      plt.plot(x_data, y_data)
      plt.gcf().autofmt_xdate()
      plt.savefig('static/test.png')
