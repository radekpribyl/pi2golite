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

from .sensor import Sensor


class Switch(Sensor):
    def init(self):
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self._initialized = True
