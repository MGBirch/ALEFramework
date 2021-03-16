import random

class EnergySource(Entity):
    """docstring for EnergySource."""

    def __init__(self):
        super().__init__()


    def move(self, mapSizeX, mapSizeZ):
        entityField = self.getField('translation')
        randX = random.uniform(-2.45, 2.45)
        randZ = random.uniform(-2.45, 2.45)
        newPos = [randX,0.05,randX]
        entityField.setSFVec3f(newPos)
