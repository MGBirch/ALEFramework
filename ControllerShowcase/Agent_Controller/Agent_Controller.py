from ALEFramework.Agent import Agent
class  myAgent(Agent):
    def __init__(self):
        self.mdNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
        self.objName = 'car'
        super().__init__(self.mdNames, self.objName)
        self.food = ['battery']
        self.wheels = self.getMotorDevices()
        self.infPos = float('inf')
        self.multiMoveMotorPos(self.wheels, self.infPos)
        self.setMultiMotorVel(self.wheels, 1)
     
    def behaviour(self):
        while self.robot.step(self.timestep) != -1:
            isCollision = self.checkEnergyCollision(self.food)
            if isCollision:
                self.eat(isCollision)
            elif(self.checkObstacle()):
                isObstacle = self.checkObstacle()
                self.avoidObstacle(isObstacle)
            else:
                angle = self.checkRecogniseSource()
                if angle < -0.3:
                    self.turnLeft()

                elif angle > 0.3:
                    self.turnRight()

                else:
                    self.setMultiMotorVel(self.wheels, 1)
                    

    def turnLeft(self):
        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                self.md[i].setVelocity(0.5* self.LOW_SPEED)
            else:
                self.md[i].setVelocity(0.5 * self.MAX_SPEED)
            count = count + 1
    
    def turnRight(self):
        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                self.md[i].setVelocity(0.5 * self.MAX_SPEED)
            else:
                self.md[i].setVelocity(0.5 * self.LOW_SPEED)
            count = count + 1
                  
agent = myAgent()
agent.behaviour()