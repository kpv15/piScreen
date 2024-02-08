import RPi.GPIO as GPIO
from threading import Event

from Keyboard.Button import Button


class KeyListener:
    __BOUNCE_TIME = 600

    __registered_events: dict[Button, Event] = {}

    def __init__(self):
        self.init_gpio()

    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        self.__add_button(Button.OK)
        self.__add_button(Button.RETURN)
        self.__add_button(Button.DOWN)
        self.__add_button(Button.UP)

    def __add_button(self, button: Button):
        GPIO.setup(button.value, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(button.value, GPIO.RISING, callback=self.__button_callback, bouncetime=self.__BOUNCE_TIME)

    def __button_callback(self, key_id):
        button = Button(key_id)
        print('Button ' + button.name + ' pressed')
        self.__registered_events[button].set()

    def register_event(self, button: Button, event: Event):
        self.__registered_events[button] = event
