


class Agent(Entity):
    """docstring for Agent."""

    def __init__(self, pos, robot):
        super().__init__(pos)
        self.energy = 10000
        self.isAlive = True
        self.timestep = robot.getBasicTimeStep()
        self.camera = robot.getDevice('camera')
        self.camera.enable(timestep)
        self.camera.recognitionEnable(timestep)


    def multiMoveMotorPos(devices, dPos):
        i = 0
        for device in devices:
            device.setPosition(dPos)
            i=i+1

    def setMultiMotorVel(devices, vel):
        i = 0
        for device in devices:
            device.setVelocity(vel[i])
            i=i+1
