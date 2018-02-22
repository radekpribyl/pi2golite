"""
    Python Module including classes to control HW aspects of Pi2Go robot
    Provides access to basic functions of the Pi2Go robot
    No logic included in this module
    Module created by Radek Pribyl based on initial py2go file created
    by Gareth Davies and Zachary Igielman
"""

try:
    import RPi.GPIO as GPIO
except ImportError:
    import pi2golite.dummyGPIO as GPIO


class Sensor(object):
    def __init__(self, pin):
        self._pin = pin
        self._initialized = False

    def init(self):
        if not self._initialized:
            GPIO.setup(self._pin, GPIO.IN)
            self._initialized = True

    def cleanup(self):
        if self._initialized:
            self.remove_callbacks()
            GPIO.cleanup(self._pin)
            self._initialized = False

    @property
    def activated(self):
        if self._initialized:
            if GPIO.input(self._pin) == 0:
                return True
            else:
                return False

    def _generate_callback(self, callback):
        def _call_callback(pin):
            state = self.activated
            callback(self._pin, state)
        return _call_callback

    def register_off_callback(self, callback, bouncetime=100):
        if self._initialized:
            fce_to_call = self._generate_callback(callback)
            GPIO.add_event_detect(self._pin, GPIO.RISING, callback=fce_to_call,
                                  bouncetime=bouncetime)
            return True
        else:
            return False

    def register_on_callback(self, callback, bouncetime=100):
        if self._initialized:
            fce_to_call = self._generate_callback(callback)
            GPIO.add_event_detect(self._pin, GPIO.FALLING, callback=fce_to_call,
                                  bouncetime=bouncetime)
            return True
        else:
            return False

    def register_both_callbacks(self, callback, bouncetime=100):
        if self._initialized:
            fce_to_call = self._generate_callback(callback)
            GPIO.add_event_detect(self._pin, GPIO.BOTH, callback=fce_to_call,
                                  bouncetime=bouncetime)
            return True
        else:
            return False

    def remove_callbacks(self):
        if self._initialized:
            GPIO.remove_event_detect(self._pin)
