class Pi2GoLiteConfig(object):
    """
    Configuration class which provides default configuration
    Either subclass it or modify the values in the instance
    and pass it to Robot class
    """
    motor_left = {'fwdpin': 7, 'revpin': 8, 'fwdcorr': 0, 'revcorr': 0}
    motor_right = {'fwdpin': 10, 'revpin': 9, 'fwdcorr': 0, 'revcorr': 0}
    front_led = {'pin': 22}
    rear_led = {'pin': 23}
    obstacle_left = {'pin': 4}
    obstacle_right = {'pin': 17}
    linesensor_left = {'pin': 18}
    linesensor_right = {'pin': 27}
    switch = {'pin': 11}
    distance_sensor = {'pin': 14}
    wheelsensors = {'avail': False,
                    'measure_param': {'whl_diameter': 6.5, 'robot_width': 12,
                                      'numsteps': 16}}
    servos = {'avail': False,
              'param': {'panpin': 24, 'tiltpin': 25, 'idletimeout': 2000,
                        'minsteps': 50, 'maxsteps': 250, 'panmaxangle': 180,
                        'tiltmaxangle': 180}}
