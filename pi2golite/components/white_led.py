"""
    Python Module including classes to control HW aspects of Pi2Go robot
    Provides access to basic functions of the Pi2Go robot
    No logic included in this module
    Module created by Radek Pribyl based on initial py2go file created
    by Gareth Davies and Zachary Igielman
"""
import time
try:
    import RPi.GPIO as GPIO
except ImportError:
    import pi2golite.dummyGPIO as GPIO

from pi2golite._helpers import validate_max


class WhiteLED(object):
    def __init__(self, pin):
        self._pin = pin
        self._pwm = None
        self._initialized = False

    def init(self):
        if not self._initialized:
            GPIO.setup(self._pin, GPIO.OUT)
            self._pwm = GPIO.PWM(self._pin, 100)
            self._pwm.start(0)
            self._initialized = True

    def cleanup(self):
        if self._initialized:
            self.off()
            GPIO.cleanup(self._pin)
            self._initialized = False

    def on(self):
        self.set(100)

    def off(self):
        self.set(0)

    def set(self, intensity):
        if self._initialized:
            intensity = validate_max(100 - intensity)
            self._pwm.ChangeDutyCycle(intensity)

    def brighten(self, delay=0.1, step=5):
        for dc in range(0, 101, step):
            self.set(dc)
            time.sleep(delay)

    def dim(self, delay=0.1, step=5):
        for dc in range(100, -1, step * -1):
            self.set(dc)
            time.sleep(delay)
