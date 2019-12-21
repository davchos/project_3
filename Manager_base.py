import pygame
from pygame.locals import * 
from constantes import *

class Manager_base():
    """
        Base class 
    """
    stop = True
    d = ()
    
    def handlekey(self, d=None):
        pass

    def save_game(self):
        pass

    def display_personnage(self):
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
        temp = True
        for event in pygame.event.get():      
            if event.type == KEYDOWN:
                self.d = event
                return True
            if event.type == QUIT:
                self.stop = False
                exit()
        return False




