# File: network.py
# Author: @StupidZY

class Network:
    def __init__(self):
        self.devices = []

    def register_device(self, device):
        self.devices.append(device)

    def unregister_device(self, device):
        self.devices.remove(device)

    def get_device_by_name(self, name):
        for device in self.devices:
            if device.name == name:
                return device
        return None
