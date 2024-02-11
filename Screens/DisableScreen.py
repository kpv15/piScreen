from adafruit_ssd1306 import SSD1306_I2C
from Keyboard.KeyEvent import KeyEvent


class DisableScreen:

    def __init__(self, disp: SSD1306_I2C, input_event: KeyEvent):
        self.__disp = disp
        self.__inputEvent = input_event

    def run(self):
        self.__disp.poweroff()
        self.__inputEvent.wait()
        self.__disp.poweron()
        print("end of disable screen")
