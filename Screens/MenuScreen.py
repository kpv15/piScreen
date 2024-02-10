from PIL import Image, ImageDraw, ImageFont
from adafruit_ssd1306 import SSD1306_I2C

from Keyboard.Button import Button
from Keyboard.KeyEvent import KeyEvent


class MenuScreen:
    __LANE_HEIGHT = 10
    __menu_list = ['STATS', 'CLOCK', 'SETTINGS', 'EXIT']
    __first_printed_element = 0

    def __init__(self, disp: SSD1306_I2C, input_event: KeyEvent):
        self.__font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 10)
        self.__disp = disp
        self.__inputEvent = input_event

    def run(self):
        button = None
        current_index = 0
        while not (button is not None and (button is Button.RETURN)):
            current_index = self.__scroll_cursor(current_index, button)

            image = Image.new("1", (self.__disp.width, self.__disp.height))
            draw = ImageDraw.Draw(image)
            self.__prepare_list(draw, current_index)
            self.__disp.image(image)
            self.__disp.show()
            button = self.__inputEvent.wait()

        print("end of clock screen")

    def __scroll_cursor(self, current_index, button):
        if button is Button.UP:
            current_index -= 1
            if current_index < 0:
                current_index = len(self.__menu_list) - 1
        elif button is Button.DOWN:
            current_index += 1
            if current_index > len(self.__menu_list) - 1:
                current_index = 0
        return current_index

    def __prepare_list(self, draw, current_index):
        for i, element in enumerate(self.__menu_list):
            if i == current_index:
                label = '->' + element
            else:
                label = '  ' + element
            draw.text((0, i * self.__LANE_HEIGHT), label, fill=255, font=self.__font)
