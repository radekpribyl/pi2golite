"""
    Python Module including classes to control HW aspects of Pi2Go robot
    Provides access to basic functions of the Pi2Go robot
    No logic included in this module
    Module created by Radek Pribyl based on initial py2go file created
    by Gareth Davies and Zachary Igielman
"""
import os
from pi2golite.rpigpio.servo import Servo
from pi2golite.common import gpio_to_physical

class ServosDriver(object):
    """
    Class which starts the servod blaster and configures it
    It also initiates servos which are connected (pan and tilt)
    """

    def __init__(self, panpin, tiltpin, idletimeout, minsteps,
                 maxsteps, panmaxangle, tiltmaxangle):
        self._panpin = gpio_to_physical(panpin)
        self._tiltpin = gpio_to_physical(tiltpin)
        self._idletimeout = idletimeout
        self._minsteps = minsteps
        self._maxsteps = maxsteps
        self.pan_servo = Servo(self._panpin, self._minsteps,
                               self._maxsteps, panmaxangle)
        self.tilt_servo = Servo(self._tiltpin, self._minsteps,
                                self._maxsteps, tiltmaxangle)
        self._initialized = False

    def init(self):
        """Starts the servod and initializes both servos"""
        if not self._initialized:
            path = os.path.split(os.path.realpath(__file__))[0]
            command = ('/servod --idle-timeout=%s --min=%s --max=%s '
                       '--p1pins="%s,%s" > /dev/null') % (self._idletimeout,
                                                          self._minsteps,
                                                          self._maxsteps,
                                                          self._panpin, self._tiltpin)
            os.system(path + command)
            self.pan_servo.init()
            self.tilt_servo.init()
            self._initialized = True

    def cleanup(self):
        """Stops the servod"""
        if self._initialized:
            self.pan_servo.cleanup()
            self.tilt_servo.cleanup()
            os.system('sudo killall servod')
            self._initialized = False
