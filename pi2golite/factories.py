#This file includes helper methods used by other pi2golite files
from pi2golite.pigpio.pigpio_factory import PigpioFactory
from pi2golite.rpigpio import RpigpioFactory

def get_components_factory(config):
    if 'pigpio' in config.__dict__:
        if 'use' in config.pigpio and config.pigpio['use']:
            return PigpioFactory(config)
    return RpigpioFactory(config)
