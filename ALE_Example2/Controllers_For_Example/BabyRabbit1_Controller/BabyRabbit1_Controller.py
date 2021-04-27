from ALEFramework.LeggedPrey import LeggedPrey
class  myVehicle(LeggedPrey):
    def __init__(self):
        mdNames = ['leg1', 'leg2', 'leg3', 'leg4']
        turnSpeed = 1.0
        forSpeed = 1.0
        objName = 'BabyRabbit1'
        food = ''
        super().__init__(mdNames, forSpeed, objName, food)
        self.legs = self.getMotorDevices()
        self.infPos = float('inf')
        self.multiMoveMotorPos(self.legs, self.infPos)
        self.setMultiMotorVel(self.legs, 1)
     
    def behaviour(self):
        while self.robot.step(self.timestep) != -1:
                self.preyBehaviour()
                    
vehicle = myVehicle()
vehicle.behaviour()