from controller import Supervisor
class ALESuper():
    """docstring for ALESuper."""

    def __init__(self):
        super(ALESuper, self).__init__()
        self.robot = Supervisor()

    def checkEnergyCollision(robot, energySource):
        carPos = car.getPosition()
        carPos = np.array(carPos)
        batteryPos = battery.getPosition()
        batteryPos = np.array(batteryPos)
        dist = np.linalg.norm(carPos - batteryPos)
        if dist<0.25:
            energySource.move(mapSizeX, mapSizeZ)
        else:
            return False

    def
