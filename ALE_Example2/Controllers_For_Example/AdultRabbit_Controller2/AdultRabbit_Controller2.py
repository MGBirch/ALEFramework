from ALEFramework.AgentLegged import AgentLegged
class  myVehicle(AgentLegged):
    def __init__(self):
        mdNames = ['leg1', 'leg2', 'leg3', 'leg4']
        turnSpeed = 1.0
        forSpeed = 1.0
        objName = 'AdultRabbit2'
        super().__init__(mdNames, forSpeed, objName)
        self.legs = self.getMotorDevices()
        self.infPos = float('inf')
        self.multiMoveMotorPos(self.legs, self.infPos)
        self.setMultiMotorVel(self.legs, 1)
     
    def behaviour(self):
        while self.robot.step(self.timestep) != -1:
                self.moveForward()
                angle = self.checkRecogniseSource()
                
                isObstacle = self.checkObstacle()
                
                if isObstacle:
                    self.avoidObstacle(isObstacle)
                    
vehicle = myVehicle()
vehicle.behaviour()