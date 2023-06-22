# File: main.py
# Author: @StupidZY

from device import Device
from sensor import TemperatureSensor, HumiditySensor, MotionSensor
from actuator import LightActuator, ThermostatActuator
from scheduler import Scheduler, ScheduledTask
from network import Network
from database import Database
from user_interface import UserInterface
from logging import Logger

class AutomationSystem:
    def __init__(self):
        self.network = Network()
        self.database = Database()
        self.scheduler = Scheduler()
        self.user_interface = UserInterface(self)
        self.logger = Logger()

    def run(self):
        self.setup_devices()
        self.setup_scheduled_tasks()

        while True:
            command = self.user_interface.get_user_command()
            self.user_interface.process_user_command(command)

    def setup_devices(self):
        device1 = Device('Device 1', sensor=TemperatureSensor(), actuator=LightActuator())
        device2 = Device('Device 2', sensor=MotionSensor(), actuator=ThermostatActuator())
        self.network.register_device(device1)
        self.network.register_device(device2)

    def setup_scheduled_tasks(self):
        device1 = self.network.get_device_by_name('Device 1')
        device2 = self.network.get_device_by_name('Device 2')
        task1 = ScheduledTask(device1, lambda: device1.execute_command('turn_on'), lambda: device1.read_sensor_data() > 25)
        task2 = ScheduledTask(device2, lambda: device2.execute_command('set_temperature', 22), lambda: device2.read_sensor_data() == True)
        self.scheduler.add_task(task1)
        self.scheduler.add_task(task2)

if __name__ == '__main__':
    automation_system = AutomationSystem()
    automation_system.run()
