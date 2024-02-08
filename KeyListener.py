import RPi.GPIO as GPIO
from threading import Event


class KeyListener:
    __BOUNCE_TIME = 600

    __registered_events: dict[int, Event] = {}

    def __init__(self):
        self.init_gpio()

    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(6, GPIO.RISING, callback=self.button_callback, bouncetime=self.__BOUNCE_TIME)
        GPIO.add_event_detect(13, GPIO.RISING, callback=self.button_callback, bouncetime=self.__BOUNCE_TIME)
        GPIO.add_event_detect(19, GPIO.RISING, callback=self.button_callback, bouncetime=self.__BOUNCE_TIME)
        GPIO.add_event_detect(26, GPIO.RISING, callback=self.button_callback, bouncetime=self.__BOUNCE_TIME)

    def button_callback(self, key_id):
        print('Button ' + str(key_id) + ' pressed')
        self.__registered_events[key_id].set()

    def register_event(self, key_id: int, event: Event):
        self.__registered_events[key_id] = event
