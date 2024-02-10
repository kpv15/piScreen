from adafruit_ssd1306 import SSD1306_I2C

import busio
import board

from Keyboard.KeyListener import KeyListener
from Screens.ClockScreen import ClockScreen

WIDTH = 128
HEIGHT = 32
LINE_HEIGHT = 12

if __name__ == "__main__":
    i2c = busio.I2C(board.SCL, board.SDA)
    disp = SSD1306_I2C(WIDTH, HEIGHT, i2c)

    key_listener = KeyListener()
    clock_screen = ClockScreen(disp, key_listener.inputEvent)
    clock_screen.run()

    disp.poweroff()
    print("end of main thread")
