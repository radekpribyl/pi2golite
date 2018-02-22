try:
    import RPi.GPIO as GPIO
except ImportError:
    import pi2golite.dummyGPIO as GPIO

from .motor import Motor
from .sensor import Sensor
from .distance_sensor import DistanceSensor
from .wheel_sensor import WheelSensor
from .servo import Servo
from .servos_driver import ServosDriver
from .switch import Switch
from .white_led import WhiteLED

GPIO.setmode(GPIO.BOARD)