"""
This modules defines behaviours for Pi2Go Lite robot

Author: Radek Pribyl
"""
import time


class StepSteering(object):
    """
    Class defining movement actions of Pi2Go lite using wheel counters.
    The class uses instance of Steering for performing the actual
    movements and WheelCounter instances to stop the motors after
    defined number of steps

    :param  steering: instance of Steering class for movement delegation
            whl_counter_lf: instance of WheelCounter for left motor
            whl_counter_rg: instance of WheelCounter for right motor
    """

    def __init__(self, steering, whl_counter_lf, whl_counter_rg, whl_sen_lf, whl_sen_rg):
        self._steering = steering
        self._whl_counter_lf = whl_counter_lf
        self._whl_counter_rg = whl_counter_rg
        self._whl_sen_lf = whl_sen_lf
        self._whl_sen_rg = whl_sen_rg
        self._lf_motor_running = False
        self._rg_motor_running = False

    def _wait_while_running(self):
        while self._lf_motor_running and self._rg_motor_running:
            time.sleep(0.01)
        self._steering.stop()

    def _stop_left(self):
        self._steering.stop_left()
        self._lf_motor_running = False

    def _stop_right(self):
        self._steering.stop_right()
        self._rg_motor_running = False

    def _run_both_motors(self, action, steps):
        if steps > 0:
            self._lf_motor_running = True
            self._rg_motor_running = True
            self._whl_counter_lf.start(steps, self._stop_left)
            self._whl_counter_rg.start(steps, self._stop_right)
            action()
            self._wait_while_running()

    def _run_left_motor(self, action, steps, *args):
        if steps > 0:
            self._lf_motor_running = True
            self._whl_counter_lf.start(steps, self._stop_left)
            action(*args)
            self._wait_while_running()

    def _run_right_motor(self, action, steps, *args):
        if steps > 0:
            self._rg_motor_running = True
            self._whl_counter_rg.start(steps, self._stop_right)
            action(*args)
            self._wait_while_running()

    def _run_and_count(self, action, lf_steps, rg_steps):
        #Init - prepare
        if lf_steps < 0:
            lf_steps = 0

        if rg_steps < 0:
            rg_steps = 0

        lf_count = 0
        rg_count = 0
        lf_lst_pos = self._whl_sen_lf.activated
        rg_lst_pos = self._whl_sen_rg.activated
        action()

        while lf_count < lf_steps or rg_count < rg_steps:
            time.sleep(0.002)
            lf_cur_pos = self._whl_sen_lf.activated
            if lf_cur_pos != lf_lst_pos:
                lf_count += 1
                lf_lst_pos = lf_cur_pos
                if lf_count >= lf_steps:
                    self._stop_left()

            rg_cur_pos = self._whl_sen_rg.activated
            if rg_cur_pos != rg_lst_pos:
                rg_count += 1
                rg_lst_pos = rg_cur_pos
                if rg_count >= rg_steps:
                    self._stop_right()

        self._steering.stop()

    def forward(self, steps):
        #self._run_both_motors(self._steering.forward, steps)
        self._run_and_count(self._steering.forward, steps, steps)

    def reverse(self, steps):
        #self._run_both_motors(self._steering.reverse, steps)
        self._run_and_count(self._steering.reverse, steps, steps)

    def spin_left(self, steps):
        #self._run_both_motors(self._steering.spin_left, steps)
        self._run_and_count(self._steering.spin_left, steps, steps)

    def spin_right(self, steps):
        #self._run_both_motors(self._steering.spin_right, steps)
        self._run_and_count(self._steering.spin_right, steps, steps)

    def turn_left(self, steps):
        #self._run_right_motor(self._steering.turn_left, steps, 0)
        def action(): return self._steering.turn_left(0)
        self._run_and_count(action, 0, steps)

    def turn_right(self, steps):
        #self._run_left_motor(self._steering.turn_right, steps, 0)
        def action(): return self._steering.turn_right(0)
        self._run_and_count(action, steps, 0)

    def turn_rev_left(self, steps):
        #self._run_right_motor(self._steering.turn_rev_left, steps, 0)
        def action(): return self._steering.turn_rev_left(0)
        self._run_and_count(action, 0, steps)

    def turn_rev_right(self, steps):
        #self._run_left_motor(self._steering.turn_rev_right, steps, 0)
        def action(): return self._steering.turn_rev_right(0)
        self._run_and_count(action, steps, 0)
