# File: device.py
# Author: @StupidZY

class Device:
    def __init__(self, name, sensor=None, actuator=None):
        self.name = name
        self.sensor = sensor
        self.actuator = actuator

    def has_sensor(self):
        return self.sensor is not None

    def read_sensor_data(self):
        if self.has_sensor():
            return self.sensor.read_data()
        return None

    def execute_command(self, command, *args):
        if self.actuator is not None:
            getattr(self.actuator, command)(*args)
