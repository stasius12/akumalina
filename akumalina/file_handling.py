from datetime import datetime

class FileHandler(object):
    def read_temperatures_data(self):
        data = {}

        with open('akumalina/temperatures/data_temp.dat', 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                line = line.split(' ')
                date, temp = line
                try:
                    date = datetime.strptime(date, '%Y-%m-%dT%H:%M')
                except ValueError:
                                    pass
                temp = temp.strip('\n')
                data[date] = temp
        return sorted(data.items())
        
