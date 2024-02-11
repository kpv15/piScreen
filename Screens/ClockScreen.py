from PIL import Image, ImageDraw, ImageFont
from adafruit_ssd1306 import SSD1306_I2C

import time

from Keyboard.Button import Button
from Keyboard.KeyEvent import KeyEvent


class ClockScreen:

    def __init__(self, disp: SSD1306_I2C, input_event: KeyEvent):
        self.__font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 26)
        self.__disp = disp
        self.__inputEvent = input_event
        self.__SLEEP_TIME = 0.2

    def run(self):
        button = None
        while not (button is not None and button is Button.RETURN):
            image = Image.new("1", (self.__disp.width, self.__disp.height))
            draw = ImageDraw.Draw(image)
            draw.text((0, 1 + 0), time.strftime("%H:%M:%S", time.gmtime()), font=self.__font, fill=255)
            self.__disp.image(image)
            self.__disp.show()

            button = self.__inputEvent.wait(self.__SLEEP_TIME)

        print("end of clock screen")
