"""
This modules defines behaviours for Pi2Go Lite robot

Author: Radek Pribyl
"""

from pi2golite._helpers import validate_max


class Steering(object):
    """
    Class defining basic movement actions of Pi2Go lite in
    various directions. It also takes care about robot's speed

    :param  lf_motor: instance of Motor class defining left motor
            rg_motor: instance of Motor class defining right motor
            init_speed: initial speed of the robot. Speed can be in
            range of 0 to 100
    """

    def __init__(self, lf_motor, rg_motor, init_speed=20):
        self._left_motor = lf_motor
        self._right_motor = rg_motor
        self._curr_speed = init_speed
        self._last_action = self.stop
        self._last_action_arguments = None

    def cleanup(self):
        self._left_motor.cleanup()
        self._right_motor.cleanup()

    @property
    def current_speed(self):
        return self._curr_speed

    def _exec_last_action(self):
        if self._last_action_arguments is None:
            self._last_action()
        else:
            self._last_action(**self._last_action_arguments)

    def _go_forward(self, lf_speed, rg_speed):
        self._left_motor.forward(lf_speed)
        self._right_motor.forward(rg_speed)

    def _go_reverse(self, lf_speed, rg_speed):
        self._left_motor.reverse(lf_speed)
        self._right_motor.reverse(rg_speed)

    def stop(self):
        self._left_motor.stop()
        self._right_motor.stop()
        self._last_action = self.stop
        self._last_action_arguments = None

    def stop_left(self):
        self._left_motor.stop()

    def stop_right(self):
        self._right_motor.stop()

    def forward(self):
        self._go_forward(self._curr_speed, self._curr_speed)
        self._last_action = self.forward
        self._last_action_arguments = None

    def reverse(self):
        self._go_reverse(self._curr_speed, self._curr_speed)
        self._last_action = self.reverse
        self._last_action_arguments = None

    def spin_left(self):
        self._left_motor.reverse(self._curr_speed)
        self._right_motor.forward(self._curr_speed)
        self._last_action = self.spin_left
        self._last_action_arguments = None

    def spin_right(self):
        self._left_motor.forward(self._curr_speed)
        self._right_motor.reverse(self._curr_speed)
        self._last_action = self.spin_right
        self._last_action_arguments = None

    def turn_left(self, lf_pct=50):
        lf_speed = float(validate_max(lf_pct)) / 100 * self._curr_speed
        self._go_forward(lf_speed, self._curr_speed)
        self._last_action = self.turn_left
        self._last_action_arguments = {'lf_pct': lf_pct}

    def turn_right(self, rg_pct=50):
        rg_speed = float(validate_max(rg_pct)) / 100 * self._curr_speed
        self._go_forward(self._curr_speed, rg_speed)
        self._last_action = self.turn_right
        self._last_action_arguments = {'rg_pct': rg_pct}

    def turn_rev_left(self, lf_pct=50):
        lf_speed = float(validate_max(lf_pct)) / 100 * self._curr_speed
        self._go_reverse(lf_speed, self._curr_speed)
        self._last_action = self.turn_rev_left
        self._last_action_arguments = {'lf_pct': lf_pct}

    def turn_rev_right(self, rg_pct=50):
        rg_speed = float(validate_max(rg_pct)) / 100 * self._curr_speed
        self._go_reverse(self._curr_speed, rg_speed)
        self._last_action = self.turn_rev_right
        self._last_action_arguments = {'rg_pct': rg_pct}

    def set_speed(self, speed):
        speed = validate_max(speed)
        self._curr_speed = speed
        self._exec_last_action()
        return self._curr_speed

    def increase_speed(self, increment=10):
        speed = self._curr_speed + increment
        return self.set_speed(speed)

    def decrease_speed(self, decrement=10):
        speed = self._curr_speed - decrement
        return self.set_speed(speed)
