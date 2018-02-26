import abc
ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()}) 

class ComponentFactory(ABC):
    def __init__(self, pi2golite_config):
        self._config = pi2golite_config
        self._cache = {}

    def _create_component(self, comp_name, comp_create):
        component_config = getattr(self._config, comp_name, {})

        if not component_config:
             raise ValueError("No configuration for {1}".format(comp_name))
        
        if comp_name not in self._cache:
            self._cache[comp_name] = comp_create(component_config)

        return self._cache[comp_name]

    def _create_component_position(self, comp_name, position, comp_create):
        component_config = getattr(self._config, comp_name, {})

        if position not in component_config:
            raise ValueError("No {0} configuration for {1}".format(comp_name, position))

        cache_key = comp_name + str(position.value)
        if cache_key not in self._cache:
            self._cache[cache_key] = comp_create(component_config[position])

        return self._cache[cache_key]

    def create_motor(self, position):
        return self._create_component_position("motors", position, self._create_motor)

    def create_led(self, position):
        return self._create_component_position("leds", position, self._create_led)

    def create_obstacle_sensor(self, position):
        return self._create_component_position("obstacle_sensors", position, self._create_obstacle_sensor)

    def create_line_sensor(self, position):
        return self._create_component_position("line_sensors", position, self._create_line_sensor)

    def create_wheel_sensor(self, position):
        line_sensor = self._create_component_position("line_sensors", position, self._create_line_sensor)
        return self._create_wheel_sensor(line_sensor)

    def create_distance_sensor(self):
        return self._create_component("distance_sensor", self._create_distance_sensor)

    def create_switch(self):
        return self._create_component("switch", self._create_switch)

    def create_servo(self, position):
        pass

    @abc.abstractmethod
    def _create_motor(self, config):
        pass

    @abc.abstractmethod
    def _create_led(self, config):
        pass

    @abc.abstractmethod
    def _create_obstacle_sensor(self, config):
        pass

    @abc.abstractmethod
    def _create_line_sensor(self, config):
        pass

    @abc.abstractmethod
    def _create_wheel_sensor(self, line_sensor):
        pass

    @abc.abstractmethod
    def _create_distance_sensor(self, config):
        pass

    @abc.abstractmethod
    def _create_switch(self, config):
        pass
