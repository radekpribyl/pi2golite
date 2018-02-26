"""
This modules defines behaviours for Pi2Go Lite robot

Author: Radek Pribyl
"""
import math

from pi2golite.common import validate_max

class MeasureSteering(object):
    """
    Class defining movement actions of Pi2Go lite using distance unit
    (if class initiated with whl_diameter and robot_width e.g. in centimeters
    then the distance should be in centimeters too). Angles are to be provided
    in degrees (in range of 0 to 360)
    The class recalculates the distance units and ange degrees to steps and
    delegates to instance of StepSteering to perform the movement

    :param  step_steering: instance of StepSteering class for movement delegation
            whl_diameter: diameter of the wheel - default wheels should be 65 mm / 6.5 cm
            robot_width: width of the robot - used in angles calculation
            numsteps: number of steps on WheelCounter. Provided wheelcounters have 16 steps

    Please note that the precision of the movement is determined by the number of steps on
    wheelcounters so it cannot be 100% precise.
    """

    def __init__(self, step_steering, whl_diameter, robot_width, numsteps):
        self._step_steering = step_steering
        self._robot_width = robot_width
        self._step_dist = math.pi * whl_diameter / numsteps

    def _calc_steps_from_dist(self, dist):
        return round(dist / self._step_dist)

    def _calc_steps_from_angle(self, angle, spin=False):
        angle = validate_max(angle, 360)
        # For turning the robot width is radius, for spin diameter
        if spin:
            const = 1
        else:
            const = 2
        return angle * math.pi * const * self._robot_width / 360 / self._step_dist

    def forward(self, distance):
        if distance > 0:
            steps = self._calc_steps_from_dist(distance)
            self._step_steering.forward(steps)

    def reverse(self, distance):
        if distance > 0:
            steps = self._calc_steps_from_dist(distance)
            self._step_steering.reverse(steps)

    def spin_left(self, angle):
        steps = self._calc_steps_from_angle(angle, True)
        self._step_steering.spin_left(steps)

    def spin_right(self, angle):
        steps = self._calc_steps_from_angle(angle, True)
        self._step_steering.spin_right(steps)

    def turn_left(self, angle):
        steps = self._calc_steps_from_angle(angle)
        self._step_steering.turn_left(steps)

    def turn_right(self, angle):
        steps = self._calc_steps_from_angle(angle)
        self._step_steering.turn_right(steps)

    def turn_rev_left(self, angle):
        steps = self._calc_steps_from_angle(angle)
        self._step_steering.turn_rev_left(steps)

    def turn_rev_right(self, angle):
        steps = self._calc_steps_from_angle(angle)
        self._step_steering.turn_rev_right(steps)
