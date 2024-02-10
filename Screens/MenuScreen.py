from PIL import Image, ImageDraw, ImageFont
from adafruit_ssd1306 import SSD1306_I2C

from Keyboard.Button import Button
from Keyboard.KeyEvent import KeyEvent


class MenuScreen:
    __LANE_HEIGHT = 10
    __first_printed_element = 0
    __current_index = 0

    def __init__(self, disp: SSD1306_I2C, input_event: KeyEvent, elements_list: list):
        self.__font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 10)
        self.__disp = disp
        self.__inputEvent = input_event
        self.__menu_list = elements_list

    def get_selection(self):
        button = None
        while not (button is not None and (button is Button.RETURN)):
            self.__scroll_cursor(button)
            self.__scroll_list()

            image = Image.new("1", (self.__disp.width, self.__disp.height))
            draw = ImageDraw.Draw(image)
            self.__prepare_list(draw)
            self.__disp.image(image)
            self.__disp.show()
            button = self.__inputEvent.wait()

        print("end of clock screen")

    def __scroll_cursor(self, button):
        if button is Button.UP:
            self.__current_index -= 1
            if self.__current_index < 0:
                self.__current_index = len(self.__menu_list) - 1
        elif button is Button.DOWN:
            self.__current_index += 1
            if self.__current_index > len(self.__menu_list) - 1:
                self.__current_index = 0

    def __scroll_list(self):
        print("curr: " + str(self.__current_index) + " first: " + str(self.__first_printed_element))
        if self.__current_index - self.__first_printed_element > 2:
            self.__first_printed_element += 1
        elif self.__current_index - self.__first_printed_element < 0:
            self.__first_printed_element -= 1

    def __prepare_list(self, draw):
        for i, element in enumerate(self.__menu_list):
            position_on_screen = i - self.__first_printed_element
            if i == self.__current_index:
                label = '->' + element
            else:
                label = '  ' + element
            draw.text((0, position_on_screen * self.__LANE_HEIGHT), label, fill=255, font=self.__font)
