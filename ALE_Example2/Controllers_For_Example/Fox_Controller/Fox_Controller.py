from ALEFramework.AgentVehicle import AgentVehicle
class  Fox(AgentVehicle):
    def __init__(self):
        mdNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
        turnSpeed = 1.0
        forSpeed = 1.0
        objName = 'Fox'
        super().__init__(mdNames, turnSpeed, forSpeed, objName)
        self.food = ['AdultRabbit','AdultRabbit1','AdultRabbit2','BabyRabbit','BabyRabbit1']
        self.wheels = self.getMotorDevices()
        self.infPos = float('inf')
        self.multiMoveMotorPos(self.wheels, self.infPos)
        self.setMultiMotorVel(self.wheels, 1)
        self.setMaxEnergy(100000)
        self.setEnergy(100000)
        self.setConsumptionEnergy(20000)
     
    def behaviour(self):
        while self.robot.step(self.timestep) != -1:
            if self.energy > 0:
                self.energy = self.energy -1
                self.moveForward()
                if self.energy < 100000:
                    isCollision = self.checkEnergyCollision(self.food)
                    if isCollision:
                        self.eat(isCollision)
                    angle = self.checkRecogniseSource()
                    if angle < -0.1:
                        self.turnSlowLeft()
            
                    elif angle > 0.1:
                        self.turnSlowRight()
            
                    elif angle <= 0.1 and angle >= -0.1:
                        self.moveForward()
                
                isObstacle = self.checkObstacle()
                
                if isObstacle:
                    self.avoidObstacle(isObstacle)
                
            else:
                self.setMultiMotorVel(self.wheels, 0)
fox = Fox()
fox.behaviour()