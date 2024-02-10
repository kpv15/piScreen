from adafruit_ssd1306 import SSD1306_I2C

import busio
import board

from Keyboard.KeyListener import KeyListener
from Screens.ClockScreen import ClockScreen
from Screens.MenuScreen import MenuScreen

WIDTH = 128
HEIGHT = 32


def init_display():
    i2c = busio.I2C(board.SCL, board.SDA)
    return SSD1306_I2C(WIDTH, HEIGHT, i2c)


def start_menu(menu_map: dict, block_exit_by_return_button=True):
    menu_screen = MenuScreen(disp, key_listener.inputEvent, list(menu_map.keys()), block_exit_by_return_button)
    while True:
        selected_element_label = menu_screen.get_selection()
        if selected_element_label is None:
            break

        selected_element = menu_map[selected_element_label]
        if isinstance(selected_element, dict):
            start_menu(selected_element, block_exit_by_return_button=False)
        else:
            selected_element.run()


if __name__ == "__main__":
    disp = init_display()
    key_listener = KeyListener()

    program_menu_map = {
        'CLOCK': ClockScreen(disp, key_listener.inputEvent),
        'SUB_MENU': {
            'TEST': None,
            'TEST2': None
        }
    }

    try:
        start_menu(program_menu_map)
    except Exception as e:
        disp.poweroff()
        raise e

    disp.poweroff()
    print("end of main thread")
