import pygame
from pygame.locals import * 
from constantes import *

class Manager_base():
    """
        Base class 
    """
    stop = True
    d = ()
    #def __init__(self):
    #    pygame.init()
    #    self.window = pygame.display.set_mode((cote_fenetre, cote_fenetre))

    #def getuserinput(self):  
    #    for event in pygame.event.get():      
    #        if event.type == KEYDOWN:
    #            if event.key in [UP, DOWN, LEFT, RIGHT]:
    #                self.d = event.key
    #        if event.key == 'Q':
    #            self.stop = False
    #            self.save_game()
    #            exit() 

    def handlekey(self, d=None):
        pass

    def save_game(self):
        pass

    def display(self):
        pass
    
    def play(self):
        while self.stop:
            pygame.time.Clock().tick(30)
            if self.getuserinput():
                self.handlekey()    
            self.display()
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




