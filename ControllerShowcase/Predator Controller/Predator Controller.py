from ALEFramework.LeggedPredator import LeggedPredator
class  myAnimal(LeggedPredator):
    def __init__(self):
        mdNames = ['leg1', 'leg2', 'leg3', 'leg4']
        turnSpeed = 1.0
        forSpeed = 1.0
        objName = 'animal'
        preyName = ['battery']
        super().__init__(mdNames, turnSpeed, forSpeed, objName, preyName)
        self.wheels = self.getMotorDevices()
        self.infPos = float('inf')
        self.multiMoveMotorPos(self.wheels, self.infPos)
        self.setMultiMotorVel(self.wheels, 1)
     
    def behaviour(self):
        while self.robot.step(self.timestep) != -1:

            if self.getEnergy() != 0:
                self.predBehaviour()
                    
animal = myAnimal()
animal.behaviour()