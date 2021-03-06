"""
Class to handle pernnage
"""
from const import UP, DOWN, LEFT, RIGHT

class Personnage(object):
    """ Personnage class """
    def __init__(self):
        self.position = (0, 0)
        self.old_position = (0, 0)
        self.bag = 0

    def move(self, user_key):
        """ K_*, * = UP/DOWN/RIGHT/LEFT with pygame """
        if user_key.key == UP:
            return -1, 0
        elif user_key.key == DOWN:
            return 1, 0
        elif user_key.key == LEFT:
            return 0, -1
        elif user_key.key == RIGHT:
            return 0, 1
        return 0, 0

    def update_pos(self, pos):
        """ Manage personnage's position"""
        self.old_position = self.position
        self.position = pos

    def update_bag(self):
        """Manage personnage's tool """
        self.bag += 1
