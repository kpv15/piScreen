import RPi.GPIO as GPIO

from Keyboard.Button import Button
from Keyboard.KeyEvent import KeyEvent


class KeyListener:
    __BOUNCE_TIME = 200
    inputEvent = KeyEvent()

    def __init__(self):
        self.__init_gpio()

    def __init_gpio(self):
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
        self.inputEvent.set(button)

