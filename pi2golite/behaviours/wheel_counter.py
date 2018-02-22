"""
This modules defines behaviours for Pi2Go Lite robot

Author: Radek Pribyl
"""


class WheelCounter(object):
    """ 

    """

    def __init__(self, whlsensor):
        self._whlsensor = whlsensor
        self._counting = False
        self._count = 0
        self._target = 0
        self._finish_callback = None

    @property
    def count(self):
        return self._count

    def init(self):
        pass

    def cleanup(self):
        if self._counting:
            self._stop

    def start(self, target, callback):

        if self._counting:
            print('Already running')
        else:
            if not callable(callback):
                raise AttributeError('callback is not callable')
            self._finish_callback = callback
            self._count = 0
            self._target = int(round(target))
            res = self._whlsensor.register_both_callbacks(self._callback, 20)
            if res:
                self._counting = True
            else:
                print('Sensor not initiated')

    def _stop(self):
        if self._counting:
            self._whlsensor.remove_callbacks()
            self._finish_callback()
            self._finish_callback = None
            self._counting = False

    def _callback(self, pin, state):
        self._count += 1
        if self._count >= self._target:
            self._stop()
