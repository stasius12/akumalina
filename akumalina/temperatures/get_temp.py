import sys
from datetime import datetime
from w1thermsensor import W1ThermSensor

class Temperature(object):
    def __init__(self):
        self.sensor = W1ThermSensor()

    def get_temperature(self, unit='C', date=True):
        unit = self.sensor.DEGREES_C if unit == 'C' else self.sensor.DEGREES_F
        if date:
            date_today = datetime.today().strftime('%H:%M')
            return (date_today, self.sensor.get_temperature(unit=unit))
        return self.sensor.get_temperature(unit=unit)

if __name__ == '__main__':
    unit = sys.argv[1] if len(sys.argv) > 1 else 'C'
    date=True
    temp = Temperature().get_temperature(unit=unit, date=True)
    if date:
        print('%s %s' % (temp[0], temp[1]))
    else:
        print(temp)

