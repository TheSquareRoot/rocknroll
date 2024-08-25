class Flow:
    def __init__(self, friction_vel, kin_visco, duration, step):
        self.friction_vel = friction_vel
        self.kin_visco = kin_visco
        self.duration = duration
        self.step = step
