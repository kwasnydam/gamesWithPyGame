import pygame

class Obstacle:
    """A class representing a flying obstacle in our game"""

    def __init__(self, width=50, height=50, x=0, y=0, color=(255, 0, 0)):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color


