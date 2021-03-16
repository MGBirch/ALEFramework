import cv2
import numpy as np
import math
import random

from controller import Robot, Supervisor, Node

class Entity(object):
    """docstring for Entity."""

    def __init__(self):
        self.robot = Supervisor()

    def getPosition(self, name):
        thing = self.robot.getFromDef(name)
        pos = thing.getPosition()
        return pos
