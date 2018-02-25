from pi2golite.common import LEFT, RIGHT, FRONT, REAR
class Pi2GoLiteConfig(object):
    """
    Configuration class which provides default configuration
    Either subclass it or modify the values in the instance
    and pass it to Robot class
    """
    motors = {
        LEFT : {'fwdpin': 7, 'revpin': 8, 'fwdcorr': 0, 'revcorr': 0},
        RIGHT : {'fwdpin': 10, 'revpin': 9, 'fwdcorr': 0, 'revcorr': 0}
    }
    leds = {
        FRONT : {'pin': 22},
        REAR : {'pin': 23}
    }
    obstacle_sensors = {
        LEFT : {'pin': 4},
        RIGHT : {'pin': 17}
    }
    line_sensors = {
        LEFT : {'pin': 18},
        RIGHT : {'pin': 27}
    }
    switch = {'pin': 11}
    distance_sensor = {'pin': 14}
    wheelsensors = {'avail': False,
                    'measure_param': {'whl_diameter': 6.5, 'robot_width': 12,
                                      'numsteps': 16}}
    servos = {'avail': False,
              'param': {'panpin': 24, 'tiltpin': 25, 'idletimeout': 2000,
                        'minsteps': 50, 'maxsteps': 250, 'panmaxangle': 180,
                        'tiltmaxangle': 180}}
