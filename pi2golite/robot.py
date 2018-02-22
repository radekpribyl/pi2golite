from pi2golite.components import DistanceSensor, Motor, Sensor, Switch, \
    WhiteLED, WheelSensor, ServosDriver
from pi2golite.behaviours import Steering, StepSteering, MeasureSteering, WheelCounter
from pi2golite.pi2golite_config import Pi2GoLiteConfig


class Robot(object):
    """
    The Robot class assebles all the individual components together
    and adds basic behaviours to the pi2golite robot

    :param cfg:  Instance of Pi2GoLiteConfig. If none then default
                configuration is used
    """

    def __init__(self, cfg=None):
        self.is_robot_initiated = False

        if not isinstance(cfg, Pi2GoLiteConfig) or cfg is None:
            cfg = Pi2GoLiteConfig()

        # Defining robot's hardware components
        self.components = {}

        # Both motor setup
        motor_left = Motor(**cfg.motor_left)
        motor_right = Motor(**cfg.motor_right)

        self.components['left_motor'] = motor_left
        self.components['right_motor'] = motor_right

        # While LEDs setup
        self.components['front_led'] = WhiteLED(**cfg.front_led)
        self.components['rear_led'] = WhiteLED(**cfg.rear_led)

        # IR sensors
        self.components['obstacle_left'] = Sensor(**cfg.obstacle_left)
        self.components['obstacle_right'] = Sensor(**cfg.obstacle_right)
        self.components['linesensor_left'] = Sensor(**cfg.linesensor_left)
        self.components['linesensor_right'] = Sensor(**cfg.linesensor_right)

        # Switch
        self.components['switch'] = Switch(**cfg.switch)

        # Distance sensor
        self.components['distance_sensor'] = DistanceSensor(
            **cfg.distance_sensor)

        # Optional components
        # Aliases for wheel sensors as they have to be switched
        # Pins are the same as for line sensors
        self._whl_counters_avail = cfg.wheelsensors['avail']
        if self._whl_counters_avail:
            whl_sen_lf = WheelSensor(self.components['linesensor_left'])
            whl_sen_rg = WheelSensor(self.components['linesensor_right'])
            self.components['wheelsensor_left'] = whl_sen_lf
            self.components['wheelsensor_right'] = whl_sen_rg
            whl_cntr_lf = WheelCounter(whl_sen_lf)
            whl_cntr_rg = WheelCounter(whl_sen_rg)
            self.components['wheelcounter_left'] = whl_cntr_lf
            self.components['wheelcounter_right'] = whl_cntr_rg

        # Servos
        if cfg.servos['avail']:
            self.components['servos'] = ServosDriver(**cfg.servos['param'])

        # Adding behaviour
        self.steering = Steering(motor_left, motor_right)

        if self._whl_counters_avail:
            self.step_steering = StepSteering(
                self.steering, whl_cntr_lf, whl_cntr_rg, whl_sen_lf, whl_sen_rg)
            self.measure_steering = MeasureSteering(self.step_steering,
                                                    **cfg.wheelsensors['measure_param'])

    def __getattr__(self, attrname):
        """"Delegate to steering instance to simplify access to key robot's methods"""

        if self._whl_counters_avail:
            # Prefix step_ is used for step_steering so try it
            if attrname.startswith('step_'):
                attr = attrname[5:]
                if attr in (n for n in dir(self.step_steering) if not n.startswith('_')):
                    return getattr(self.step_steering, attr)

            # Another allowed prefix is meas_ for meaasure_steering actions
            elif attrname.startswith('meas_'):
                attr = attrname[5:]
                if attr in (n for n in dir(self.measure_steering) if not n.startswith('_')):
                    return getattr(self.measure_steering, attr)

        # Lastly try steering and if not found raise error
        if attrname in (name for name in dir(self.steering) if not name.startswith('_')):
            return getattr(self.steering, attrname)
        else:
            raise AttributeError(attrname)

    def init(self):
        """Initialize all components connected to pi2golite robot"""
        for component in self.components.values():
            component.init()
        self.is_robot_initiated = True

    def cleanup(self):
        """Clean all components."""
        for component in self.components.values():
            component.cleanup()
        self.is_robot_initiated = False
