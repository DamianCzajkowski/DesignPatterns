class Socket:

    def __init__(self, voltage):

        self.voltage = voltage


class EuropeanSocket(Socket):

    def __init__(self):
        super().__init__(230)


class USASocket(Socket):

    def __init__(self):
        super().__init__(120)
