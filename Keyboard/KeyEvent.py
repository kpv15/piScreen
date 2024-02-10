from threading import Event

from Keyboard.Button import Button


class KeyEvent:
    __event = Event()
    __button: Button

    def set(self, button: Button) -> None:
        self.__button = button
        self.__event.set()

    def wait(self, timeout=None):
        signaled = self.__event.wait(timeout)
        if signaled:
            self.__event.clear()
            return self.__button
        else:
            return None
