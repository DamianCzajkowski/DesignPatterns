class Charger:

    def __init__(self, device, socket):
        self.device = device
        self.socket = socket

    def __transformator(self):
        if self.socket.voltage <= self.device.max_voltage:
            return self.socket.voltage
        else:
            return self.device.max_voltage

    def plug(self):
        return self.__transformator()
