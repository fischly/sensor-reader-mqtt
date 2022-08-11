
import board
import busio
import digitalio

from util.Singleton import Singleton

@Singleton
class I2CManager:
    def __init__(self):
        # connect to the I2C bus of the pi
        print('Connecting to I2C bus...')
        self.i2c = busio.I2C(board.SCL, board.SDA)

    def get_i2c(self):
        return self.i2c