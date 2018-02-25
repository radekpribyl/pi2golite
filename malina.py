from pi2golite import Pi2GoLiteConfig, Robot
from pi2golite.common import LEFT, RIGHT

class MalinaConfig(Pi2GoLiteConfig):
    def __init__(self):
        self.motors[RIGHT]['fwdcorr'] = 4.5
        self.motors[LEFT]['revcorr'] = 0
        self.wheelsensors['avail'] = True
        self.servos['avail'] = True
        self.servos['param']['maxsteps'] = 238
        self.wheelsensors['measure_param']['whl_diameter'] = 6.55

def test():
    r.set_speed(60)
    for _ in range(0, 4):
        r.meas_forward(30)
        r.meas_turn_left(90)

r = Robot(MalinaConfig())
r.init()