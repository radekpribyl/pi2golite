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

from pi2golite._helpers import validate_max


class Motor(object):
    def __init__(self, fwdpin, revpin, fwdcorr=0, revcorr=0):
        self._pin_fwd = fwdpin
        self._pin_rev = revpin
        self._pwd_fwd = None
        self._pwd_rev = None
        self._fwdcorr = 1 - (float(validate_max(fwdcorr)) / 100)
        self._revcorr = 1 - (float(validate_max(revcorr)) / 100)
        self._initialized = False

    def init(self, init_speed=20):
        if not self._initialized:
            init_speed = validate_max(init_speed)
            GPIO.setup(self._pin_fwd, GPIO.OUT)
            GPIO.setup(self._pin_rev, GPIO.OUT)
            self._pwd_fwd = GPIO.PWM(self._pin_fwd, init_speed)
            self._pwd_rev = GPIO.PWM(self._pin_rev, init_speed)
            self._pwd_fwd.start(0)
            self._pwd_rev.start(0)
            self._initialized = True

    def cleanup(self):
        if self._initialized:
            self._pwd_fwd.stop()
            self._pwd_rev.stop()
            GPIO.cleanup(self._pin_fwd)
            GPIO.cleanup(self._pin_rev)
            self._initialized = False

    def forward(self, speed):
        if self._initialized:
            speed = validate_max(speed)
            self._pwd_fwd.ChangeFrequency(speed + 5)
            self._pwd_fwd.ChangeDutyCycle(speed * self._fwdcorr)
            self._pwd_rev.ChangeDutyCycle(0)

    def reverse(self, speed):
        if self._initialized:
            speed = validate_max(speed)
            self._pwd_rev.ChangeFrequency(speed + 5)
            self._pwd_rev.ChangeDutyCycle(speed * self._revcorr)
            self._pwd_fwd.ChangeDutyCycle(0)

    def stop(self):
        if self._initialized:
            self._pwd_rev.ChangeDutyCycle(0)
            self._pwd_fwd.ChangeDutyCycle(0)
