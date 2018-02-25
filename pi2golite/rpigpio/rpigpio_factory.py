from pi2golite.abstract.component_factory import ComponentFactory

class RpigpioFactory(ComponentFactory):
    def __init__(self, pi2golite_config):
        self._config = pi2golite_config
        self._cache = {}

    def create_motor(self, position):
        pass

    def create_led(self, position):
        pass

    def create_obstacle_sensor(self, position):
        pass

    def create_line_sensor(self, position):
        pass

    def create_wheel_sensor(self, position):
        pass

    def create_distance_sensor(self):
        pass

    def create_switch(self):
        pass

    def create_servo(self, position):
        pass