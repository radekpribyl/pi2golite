try:
    import RPi.GPIO as GPIO
except ImportError:
    import pi2golite.dummyGPIO as GPIO

from pi2golite.components.motor import Motor
from pi2golite.components.sensor import Sensor
from pi2golite.components.distance_sensor import DistanceSensor
from pi2golite.components.wheel_sensor import WheelSensor
from pi2golite.components.servo import Servo
from pi2golite.components.servos_driver import ServosDriver
from pi2golite.components.switch import Switch
from pi2golite.components.white_led import WhiteLED

GPIO.setmode(GPIO.BOARD)