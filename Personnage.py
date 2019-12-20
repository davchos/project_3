
import pygame

from constantes import *

class Personnage():
    #def __init__(self, right, left, up, down):
    def __init__(self, image):
        self.position = ()
        self.new_position = [0,0]
        self.bag = 0
        
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
          
    def update_bag(self):
        self.bag += 1    

    def display_personnage(self, window):
        im_mac = pygame.image.load(image_mac).convert()
        x, y  = [i * taille_sprite for i in self.position]
        window.blit(im_mac, (y,x))




    
