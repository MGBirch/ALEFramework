from ALEFramework.AgentPrey import AgentPrey

class  myPrey(AgentPrey):
    def __init__(self):
        mdNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
        super().__init__(mdNames)
        self.wheels = self.getWheels()
        self.infPos = float('inf')
        self.multiMoveMotorPos(self.wheels, self.infPos)
        self.setMultiMotorVel(self.wheels, 1)
     
    def behaviour(self):
        while self.robot.step(self.timestep) != -1:

            if self.getEnergy() != 0:
                isObstacle = self.checkObstacle(1)
                if isObstacle:
                    pass
                else:
                    recog = self.checkRecogniseSource(1)

vehicle = myPrey()
vehicle.behaviour()