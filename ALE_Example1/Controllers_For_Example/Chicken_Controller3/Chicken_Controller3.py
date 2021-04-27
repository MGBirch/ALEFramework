from ALEFramework.LeggedPredator import LeggedPredator
class  Chicken(LeggedPredator):
    def __init__(self):
        mdNames = ['leg1', 'leg2', 'leg3', 'leg4']
        turnSpeed = 1.0
        forSpeed = 1.0
        objName = 'chicken3'
        self.food = ['grain', 'grain1', 'grain2', 'grain3']
        super().__init__(mdNames, forSpeed, objName)
        self.legs = self.getMotorDevices()
        self.infPos = float('inf')
        self.multiMoveMotorPos(self.legs, self.infPos)
        self.setMultiMotorVel(self.legs, 1)
        self.setMaxEnergy(100000)
        self.setEnergy(100000)
        self.setConsumptionEnergy(10000)
        self.setFocusAngle(0.1)
     
    def behaviour(self):
        while self.robot.step(self.timestep) != -1:
            self.energy = self.energy -1
            if self.energy > 600000:
                self.moveForward()
                isObstacle = self.checkObstacle()
                
                if isObstacle:
                    self.avoidObstacle(isObstacle)
            else:
                self.predBehaviour()
                collided = self.checkEnergyCollision(self.food)
                if collided:
                    self.eat(collided)
                    
chicken = Chicken()
chicken.behaviour()