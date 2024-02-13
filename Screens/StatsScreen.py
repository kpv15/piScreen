import psutil as psutil
from PIL import Image, ImageDraw, ImageFont
from adafruit_ssd1306 import SSD1306_I2C

from Keyboard.Button import Button
from Keyboard.KeyEvent import KeyEvent


class StatsScreen:
    def __init__(self, disp: SSD1306_I2C, input_event: KeyEvent):
        self.__LANE_HEIGHT = 11
        self.__FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
        self.__SLEEP_TIME = 5
        self.__scroll_delta = 0
        self.__disp = disp
        self.__inputEvent = input_event

    def run(self):
        button = None
        while not (button is not None and button is Button.RETURN):
            self.__scroll_screen(button)

            image = Image.new("1", (self.__disp.width, self.__disp.height))
            draw = ImageDraw.Draw(image)

            load_str = 'LOAD: %.2f %.2f %.2f' % psutil.getloadavg()
            self.__print_lane(draw, 0, load_str)

            temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
            self.__print_lane(draw, 1, u"TEMP: %.2f \N{DEGREE SIGN}C" % temp)

            MB_DIVIDER = 1024 * 1024
            used_ram = psutil.virtual_memory()[3] / MB_DIVIDER
            total_ram = psutil.virtual_memory()[0] / MB_DIVIDER
            self.__print_lane(draw, 2, "RAM: %.0f/%.0f (MB)" % (used_ram, total_ram))

            GB_DIVIDER = 1024 * 1024 * 1024
            disc_stats = psutil.disk_usage('/')
            self.__print_lane(draw, 3,
                              "DISK: %.1f/%.1f (GB)" % (disc_stats.used / GB_DIVIDER, disc_stats.total / GB_DIVIDER))

            self.__disp.image(image)
            self.__disp.show()

            button = self.__inputEvent.wait(self.__SLEEP_TIME)

        print("end of stats screen")

    def __scroll_screen(self, button: Button):
        if button is not None:
            LANES_COUNT = 4
            LANES_ON_DISP = 2
            if button is Button.UP and self.__scroll_delta < 0:
                print("Scroll DOWN")
                self.__scroll_delta += self.__LANE_HEIGHT
            elif button is Button.DOWN and self.__scroll_delta > -self.__LANE_HEIGHT * (LANES_COUNT - LANES_ON_DISP):
                print("Scroll UP")
                self.__scroll_delta -= self.__LANE_HEIGHT

    def __print_lane(self, draw: ImageDraw, lane_num: int, value: str):
        start_height = lane_num * self.__LANE_HEIGHT + self.__scroll_delta
        draw.text((0, start_height), value, fill=255, font=self.__FONT)
