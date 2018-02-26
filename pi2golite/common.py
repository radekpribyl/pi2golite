from enum import Enum

class Position(Enum):
    LEFT = 1
    RIGHT = 2
    FRONT = 3
    REAR = 4

_PIN_TO_GPIO_REV3 = [-1, -1, -1, 2, -1, 3, -1, 4, 14, -1, 15, 17, 18, 27, -1, 22, 23, -1, 24, 10, -1, 9, 25, 11, 8, -1, 7, -1, -1, 5, -1, 6, 12, 13, -1, 19, 16, 26, 20, -1, 21 ]

def gpio_to_physical(pin_number):
    try:
        return _PIN_TO_GPIO_REV3.index(pin_number)
    except ValueError:
        return -1

def physical_to_gpio(pin_number):
    if pin_number < 0 or pin_number>len(_PIN_TO_GPIO_REV3)-1:
        return -1
    return _PIN_TO_GPIO_REV3[pin_number]

def validate_max(value, maxv=100):
    if value > maxv:
        value = maxv
    elif value < 0:
        value = 0
    return value