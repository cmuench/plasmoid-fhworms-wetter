from urllib import urlopen
import datetime

class MeasurementReader(object):
    def __init__(self):
        self._url = "http://wetter.fh-worms.de/raw.php"

    def read(self):
        data = MeasurementData()
        try:
            f = urlopen(self._url)
            raw_data = f.read()
            raw_data_array = raw_data.split(';')

            data.time = str(raw_data_array[0])
            data.pressure = str(raw_data_array[2])
            data.temperature = raw_data_array[3]
            data.wind_speed = raw_data_array[4]
            data.wind_direction = raw_data_array[7]
        except:
            pass

        return data


class MeasurementData(object):
    def __init__(self):
        self._time = None
        self._temperature = None
        self._pressure = None
        self._wind_speed = None
        self._wind_direction = None

    @property
    def time(self):
        """
        @rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, value):
        # String like 20120429131101
        self._time = datetime.datetime(int(value[0:4]), int(value[4:6]), int(value[6:8]), int(value[8:10]),
            int(value[10:12]), int(value[12:14]))

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    @property
    def wind_speed(self):
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value):
        self._wind_speed = value

    @property
    def wind_direction(self):
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, value):
        self._wind_direction = value

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value):
        self._pressure = value
