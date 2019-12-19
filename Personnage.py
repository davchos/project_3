#from getkey import  keys
import pygame
#from pygame.locals import * 
from constantes import *

class Personnage():
    #def __init__(self, right, left, up, down):
    def __init__(self, image):
        self.position = ()
        self.new_position = [0,0]
        #self.image = pygame.image.load(image).convert_alpha()
        self.bag = 0
        #self.right = pygame.image.load(right).convert_alpha()
        #self.left = pygame.image.load(left).convert_alpha()
        #self.up = pygame.image.load(up).convert_alpha()
        #self.down = pygame.image.load(down).convert_alpha()
        #self.pos = image.get_rect()
        

    def move(self, user_key):
        """ K_*, * = UP/DOWN/RIGHT/LEFT with pygame """
        if user_key.key == UP:
            #self.image = self.up
            return -1,0
        elif user_key.key == DOWN:
            #self.image = self.down
            return 1,0
        elif user_key.key == LEFT:
            #self.image = self.left
            return 0,-1
        elif user_key.key == RIGHT:
            #self.image = self.right
            return 0,1
        return 0,0    

    def update_pos(self,pos):
        self.position = pos
        #self.pos = self.pos.move(pos)
          
    def update_bag(self):
        self.bag += 1    

    def display_personnage(self, window):
        im_mac = pygame.image.load(image_mac).convert()
        x = self.position[0] * taille_sprite
        y = self.position[1] * taille_sprite
        window.blit(im_mac, (y,x))




    
