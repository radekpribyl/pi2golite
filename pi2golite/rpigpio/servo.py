"""
    Python Module including classes to control HW aspects of Pi2Go robot
    Provides access to basic functions of the Pi2Go robot
    No logic included in this module
    Module created by Radek Pribyl based on initial py2go file created
    by Gareth Davies and Zachary Igielman
"""

import os
from pi2golite.common import validate_max

class Servo(object):
    def __init__(self, pin, min_steps, max_steps, max_angle):
        self._pin = pin
        self._min_steps = min_steps
        self._max_steps = max_steps
        self._max_angle = max_angle
        self._curr_angle = 0
        self._initialized = False

    def set_angle(self, angle):
        if self._initialized:
            angle = validate_max(angle, self._max_angle)
            self._curr_angle = angle
            steps = int(self._min_steps + (self._curr_angle *
                                           (self._max_steps - self._min_steps) / self._max_angle))
            command = 'echo P1-%s=%s > /dev/servoblaster' % (self._pin, steps)
            os.system(command)

    def increase_angle(self, increment=10):
        self.set_angle(self._curr_angle + increment)
        return self._curr_angle

    def decrease_angle(self, decrement=10):
        self.set_angle(self._curr_angle - decrement)
        return self._curr_angle

    def init(self):
        self._initialized = True

    def cleanup(self):
        self._initialized = False
