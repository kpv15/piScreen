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

    main_menu = {'CLOCK': ClockScreen(disp, key_listener.inputEvent)}

    menu_screen = MenuScreen(disp, key_listener.inputEvent, list(main_menu.keys()))

    while True:
        selected_element = menu_screen.get_selection()
        if selected_element is None:
            break
        else:
            main_menu[selected_element].run()

    disp.poweroff()
    print("end of main thread")

class Menu:
    pass