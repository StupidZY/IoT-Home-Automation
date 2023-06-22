# File: sensor.py
# Author: @StupidZY

class Sensor:
    def __init__(self):
        pass

    def read_data(self):
        raise NotImplementedError


class TemperatureSensor(Sensor):
    def read_data(self):
        # Implement logic to read temperature data from the sensor
        pass


class HumiditySensor(Sensor):
    def read_data(self):
        # Implement logic to read humidity data from the sensor
        pass


class MotionSensor(Sensor):
    def read_data(self):
        # Implement logic to detect motion and return corresponding data
        pass
