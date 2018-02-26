try:
    import RPi.GPIO as GPIO
except ImportError:
    import pi2golite.dummyGPIO as GPIO

from pi2golite.rpigpio.motor import Motor
from pi2golite.rpigpio.sensor import Sensor
from pi2golite.rpigpio.distance_sensor import DistanceSensor
from pi2golite.rpigpio.wheel_sensor import WheelSensor
from pi2golite.rpigpio.servo import Servo
from pi2golite.rpigpio.servos_driver import ServosDriver
from pi2golite.rpigpio.switch import Switch
from pi2golite.rpigpio.white_led import WhiteLED
from pi2golite.rpigpio.rpigpio_factory import RpigpioFactory

GPIO.setmode(GPIO.BCM)