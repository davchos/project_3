"""
Base class to manage the game
"""
import pygame
#from pygame.locals import *
from const import QUIT, KEYDOWN

class ManagerBase(object):
    """
        Base class
    """
    stop = True
    evt = ()

    def __init__(self):
        pass

    def handlekey(self):
        """ Game logic """
        pass

    def save_game(self):
        """ Save game """
        pass

    def display_personnage(self):
        """ Manage personnage display """
        pass

    def play(self):
        """
           Main loop of the game
        """
        while self.stop:
            pygame.time.Clock().tick(30)
            if self.getuserinput():
                self.handlekey()
            self.display_personnage()
            pygame.display.flip()

    def getuserinput(self):
        """ Manage user input """
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                self.evt = event
                return True
            if event.type == QUIT:
                self.stop = False
                exit()
        return False
