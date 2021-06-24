from .device import Device
from .sockets import EuropeanSocket, USASocket
from .charger import Charger

device = Device()
socket = EuropeanSocket()
charger = Charger(device, socket)
device.charge(charger.plug())
