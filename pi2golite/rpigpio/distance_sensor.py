"""
    Python Module including classes to control HW aspects of Pi2Go robot
    Provides access to basic functions of the Pi2Go robot
    No logic included in this module
    Module created by Radek Pribyl based on initial py2go file created
    by Gareth Davies and Zachary Igielman
"""
import time
import threading
try:
    import RPi.GPIO as GPIO
except ImportError:
    import pi2golite.dummyGPIO as GPIO


class DistanceSensor(object):
    def __init__(self, pin):
        self._pin = pin
        self.measure_running = threading.Event()
        self._measure_thread = None

    def init(self):
        pass

    def cleanup(self):
        if self.measure_running.is_set:
            self.stop_distance_measure()

    def _distance_measure(self, callback, delay=1):
        if delay < 0.2:
            delay = 0.2
        while self.measure_running.is_set():
            distance = self.get_distance()
            callback(distance)
            time.sleep(delay)
        GPIO.cleanup(self._pin)

    def start_distance_measure(self, callback, delay=1):
        if not self.measure_running.is_set():
            if callable(callback):
                self._measure_thread = threading.Thread(target=self._distance_measure,
                                                        args=(callback, delay))
                self.measure_running.set()
                self._measure_thread.daemon = True
                self._measure_thread.start()
            else:
                raise AttributeError()

    def stop_distance_measure(self):
        if self.measure_running.is_set():
            self.measure_running.clear()

    def get_distance(self):
        GPIO.setup(self._pin, GPIO.OUT)
        # Send 10us pulse to trigger
        GPIO.output(self._pin, True)
        time.sleep(0.00001)
        GPIO.output(self._pin, False)

        GPIO.setup(self._pin, GPIO.IN)
        pulse_start = time.time()
        count = time.time()
        pulse_end = count
        while GPIO.input(self._pin) == 0 and time.time() - count < 0.1:
            pulse_start = time.time()

        count = time.time()
        while GPIO.input(self._pin) == 1 and time.time() - count < 0.1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        return round(distance, 2)
