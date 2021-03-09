import cv2
import numpy as np
import math
import random

from controller import Robot, DistanceSensor, Motor, Camera, CameraRecognitionObject, Supervisor, Node

class Entity(Supervisor):
    """docstring for Entity."""

    def __init__(self, pos):

        self.pos = pos
        entityField = self.getField('translation')
        entityField.setSFVec3f(pos)

    def getPosition(self):
        return pos

    def setPosition(self, x, y, z):
        entityField = self.getField('translation')
        newPos = [x,y,z]
        entityField.setSFVec3f(newPos)
        pos = newPos
