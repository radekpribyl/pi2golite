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


class WheelSensor(object):
    """ The PINs for wheel sensors are shared with line detectors
    and need to be manually switched on the robot. Therefore the WheelSensor
    class needs configuration for line detector and delegates some of the
    method calls to it """

    def __init__(self, line_sensor):
        self._line_sensor = line_sensor

    def __getattr__(self, attrname):
        if attrname in (name for name in dir(self._line_sensor) if not name.startswith('_')):
            return getattr(self._line_sensor, attrname)
        else:
            raise AttributeError(attrname)
