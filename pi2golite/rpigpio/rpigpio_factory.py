from pi2golite.abstract import ComponentFactory
from pi2golite.rpigpio import Motor, Sensor, DistanceSensor, Switch, WheelSensor, WhiteLED
class RpigpioFactory(ComponentFactory):
    def __init__(self, pi2golite_config):
        super(RpigpioFactory, self).__init__(pi2golite_config)

    def _create_motor(self, config):
        return Motor(**config)

    def _create_led(self, config):
        return WhiteLED(**config)

    def _create_obstacle_sensor(self, config):
        return Sensor(**config)

    def _create_line_sensor(self, config):
        return Sensor(**config)

    def _create_wheel_sensor(self, line_sensor):
        return WheelSensor(line_sensor)

    def _create_distance_sensor(self, config):
        return DistanceSensor(**config)

    def _create_switch(self, config):
        return Switch(**config)

    def create_servo(self, position):
        pass