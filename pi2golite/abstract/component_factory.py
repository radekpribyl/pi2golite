from abc import ABC, abstractmethod

class ComponentFactory(ABC):
    def __init__(self, pi2golite_config):
        self._config = pi2golite_config
        self._cache = {}

    def create_motor(self, position):
        if position not in self._config.motors:
            raise ValueError("No Motor configuration for {0}".format(position))
        if "motor" + position not in self._cache:
            self._cache["motor" + position] = self._create_motor(self._config.motors[position])
        return self._cache["motor" + position]

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

    @abstractmethod
    def _create_motor(self, config):
        pass
