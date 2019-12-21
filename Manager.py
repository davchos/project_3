
import pygame
from pygame.locals import *
from Manager_base import Manager_base
from constantes import *

class Manager(Manager_base):

    def __init__(self, mac=None, board=None):
        self.mac = mac
        self.b = board
        self.mac.update_pos((self.b.paths[self.b.mac][-1][0], self.b.paths[self.b.mac][-1][1]))
        self.setup_pygame()
        self.b.init_board(self.window)
        pygame.display.flip() 

    def setup_pygame(self):
        """
           Iint pygame, and create the pygame window
        """
        pygame.init()
        self.window = pygame.display.set_mode((cote_fenetre, cote_fenetre))
        
              
    def handlekey(self):
        """ This function handle game logic """
        posx,posy = self.mac.move(self.d)
        if (posx,posy) == (0,0):
            return
        temp_pos = self.mac.position[0] + posx, self.mac.position[1] + posy

        """ if not on path return """
        if self.b.grid[temp_pos] == self.b.wall:
            return
        """ if on a tool """
        if self.b.grid[temp_pos] == 'H':
            self.b.grid[temp_pos] = 'S'
            self.b.grid[(self.mac.position[0], self.mac.position[1])] = ' '
            self.mac.update_pos(temp_pos)
            self.mac.update_bag()

        """ if on the path """
        if self.b.grid[temp_pos] == ' ':
            self.b.grid[(temp_pos[0], temp_pos[1])] = 'S'
            self.b.grid[(self.mac.position[0], self.mac.position[1])] = ' ' 
            self.mac.update_pos(temp_pos)   
           
        if self.b.grid[temp_pos] == 'X':
            if self.mac.bag == 3:
                exit(" you are a winner")
            else:
                exit("You are a looser !!!")    

    def display_personnage(self):
        x_old, y_old  = [i * taille_sprite for i in self.mac.old_position]
        x, y  = [i * taille_sprite for i in self.mac.position]
        if (x,y) == (0,0) or (x_old,y_old) == (0,0):
            return
        self.window.blit(self.b.im_floor, (y_old,x_old))
        self.window.blit(self.b.im_mac, (y,x))
        
            


    
