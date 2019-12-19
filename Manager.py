
import pygame
from pygame.locals import *
#from getkey import getkey, keys
from Manager_base import Manager_base
from constantes import *





class Manager(Manager_base):

    def __init__(self, mac=None, board=None):
        self.mac = mac
        self.b = board
        self.mac.update_pos((self.b.paths[self.b.mac][-1][0], self.b.paths[self.b.mac][-1][1]))
        pygame.init()
        self.window = pygame.display.set_mode((cote_fenetre, cote_fenetre))
        
        #self.mac_image = pygame.image.load(self.mac.image).convert()
        #self.wall_image = pygame.image.load(image_wall).convert()
        #self.tool_image = pygame.image.load(image_tool).convert()
        #self.gardien_image = pygame.image.load(image_gardien).convert()
        #self.floor_image = pygame.image.load(image_floor).convert()
        
        

    def handlekey(self):
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

    #def display(self):
    #    for i in range(self.b.nblig):
    #        for j in range(self.b.nbcol):
    #            print(self.b.grid[(i,j)], end='')

    def display(self):
        self.b.display_board(self.window)
        self.mac.display_personnage(self.window)
        

    def play(self):
        while self.stop:
            pygame.time.Clock().tick(30)
            if self.getuserinput():
                print("key pressed")
                self.handlekey() 
            print("calling display")    
            self.display()
            print("returning display")
            pygame.display.flip() 
            


    
