from adafruit_ssd1306 import SSD1306_I2C

import busio
import board

from Keyboard.KeyListener import KeyListener
from Screens.ClockScreen import ClockScreen
from Screens.MenuScreen import MenuScreen

WIDTH = 128
HEIGHT = 32

if __name__ == "__main__":
    i2c = busio.I2C(board.SCL, board.SDA)
    disp = SSD1306_I2C(WIDTH, HEIGHT, i2c)

    key_listener = KeyListener()
    elements_list = ['STATS', 'CLOCK', 'SETTINGS', 'EXIT']
    menu_screen = MenuScreen(disp, key_listener.inputEvent, elements_list)
    menu_screen.get_selection()

    disp.poweroff()
    print("end of main thread")
