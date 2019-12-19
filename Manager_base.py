
#from getkey import getkey, keys
import pygame
from pygame.locals import * 
from constantes import *

class Manager_base():
    """
        Base class 
    """
    stop = True
    d = ()
    

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
    
    #def play(self):
    #    while self.stop:
    #        self.getuserinput()
    #        self.handlekey() 
    #        self.display()
    def getuserinput(self):  
        temp = True
        for event in pygame.event.get():      
            if event.type == KEYDOWN:
                #pressed = pygame.event.get()
                #if pressed.key 
                #if pygame.event.get() in [UP, DOWN, LEFT, RIGHT]:
                    #print("in event.get in getuserinput fct")
                    #temp = False
                self.d = event
                return True
            if event.type == QUIT:
                self.stop = False
                self.save_game()
                exit()
        return False 



