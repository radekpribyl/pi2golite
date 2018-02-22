class Pi2GoLiteConfig(object):
    """
    Configuration class which provides default configuration
    Either subclass it or modify the values in the instance
    and pass it to Robot class
    """
    motor_left = {'fwdpin': 26, 'revpin': 24, 'fwdcorr': 0, 'revcorr': 0}
    motor_right = {'fwdpin': 19, 'revpin': 21, 'fwdcorr': 0, 'revcorr': 0}
    front_led = {'pin': 15}
    rear_led = {'pin': 16}
    obstacle_left = {'pin': 7}
    obstacle_right = {'pin': 11}
    linesensor_left = {'pin': 12}
    linesensor_right = {'pin': 13}
    switch = {'pin': 23}
    distance_sensor = {'pin': 8}
    wheelsensors = {'avail': False,
                    'measure_param': {'whl_diameter': 6.5, 'robot_width': 12,
                                      'numsteps': 16}}
    servos = {'avail': False,
              'param': {'panpin': 18, 'tiltpin': 22, 'idletimeout': 2000,
                        'minsteps': 50, 'maxsteps': 250, 'panmaxangle': 180,
                        'tiltmaxangle': 180}}
