import numpy as np
import random
from constantes import *
import pygame
from pygame.locals import * 




class Board:
    def __init__(self):
        self.numberoftools=numberoftools
        self.nbcol = nbcol
        self.nblig  = nblig
        self.explored = 0
        self.startlig = startlig
        self.startcol = startcol
        self.wall = wall
        self.grid = np.full((nblig,nbcol), self.wall)
        self.tools = []
        self.path = []
        self.paths = []
        self.mac = []
        self.explore(startlig,startcol)
        self.save_paths()
        self.setup_tools()
        self.setup_personnage()
        
    def getdirection(self,plig,pcol):
        dirs = []
        if plig - 2 > 0:
            if self.grid[(plig-2,pcol)] == self.wall:    
                dirs.append("up")
        if pcol + 2 < self.nbcol - 1:
            if self.grid[(plig,pcol+2)] == self.wall:    
                dirs.append("right")
        if plig + 2 < self.nblig - 1:
            if self.grid[(plig+2,pcol)] == self.wall:
                dirs.append("down")  
        if pcol - 2 > 0:
            if self.grid[(plig,pcol-2)] == self.wall:
                dirs.append("left")
        return dirs                            

    def digwall(self,plig,pcol):
        self.grid[(plig,pcol)] = " "
        self.path.append([plig,pcol])

    def explore(self,plig,pcol):
        self.digwall(plig,pcol)
        self.explored +=1
        while self.explored < (self.nblig * self.nbcol/2):
            dirs = self.getdirection(plig,pcol)
            print(dirs)
            if len(dirs) != 0:
                choice = random.randrange(len(dirs))
                d = dirs[choice]
                print("direction is %s",d)
                if d == "up":
                    self.digwall(plig-1,pcol)
                    self.explore(plig-2,pcol)
                if d == "right":
                    self.digwall(plig,pcol+1)
                    self.explore(plig,pcol+2)
                if d == "down":
                    self.digwall(plig+1,pcol)
                    self.explore(plig+2,pcol)
                if d == "left":
                    self.digwall(plig,pcol-1)
                    self.explore(plig,pcol-2)
            else:
                break

    def save_paths(self):
        """ Start from (startlig,startcol)
        output contains the visited nodes
        queue the current visite noted for nodes x 
        """
        last = 0
        for i in range(len(self.path)-1):
            if abs(self.path[i][0] - self.path[i+1][0]) > 1  or abs(self.path[i][1] - self.path[i+1][1]) > 1:
                print("path")
                self.paths.append(self.path[last:i+1])
                print(self.path[last:i+1])
                print()
                last = i+1

    def setup_tools(self):
        """ place randomly the tools """
        for i in range(self.numberoftools):
            n = True 
            while n:
                c = random.randrange(1,len(self.paths)) 
                b = random.randrange(1,len(self.paths[c]))
                 
                if self.paths[c][b] not in self.tools and ( c != 0 and b != 0 ) and ( c != self.mac and b < len(self.paths[c]) - 2 ):
                    self.grid[(self.paths[c][b][0],self.paths[c][b][1])] = "H"
                    self.tools.append((self.paths[c][b][0],self.paths[c][b][1]))
                    n = False

    def setup_personnage(self):
        """ place Mac and the bad guy on the board """
        self.grid[(self.paths[0][0][0],self.paths[0][0][1])] = "X"
        n = True
        while n:
            for i in range(1,len(self.paths)):
                if len(self.paths[i]) > 3:
                    self.grid[(self.paths[i][-1][0],self.paths[i][-1][1])] = "S"
                    self.mac = i
                    n = False
                    break

    def display_board(self, window):
        im_wall = pygame.image.load(image_wall).convert()
        #im_tool = pygame.image.load(image_tool).convert()
        im_gardien = pygame.image.load(image_gardien).convert()
        #im_floor = pygame.image.load(image_floor).convert()
        window = window

        for i in range(nblig):
            for j in range(nbcol):
                y = i * taille_sprite
                x = j * taille_sprite
                print(self.grid[(i,j)])
                print(x,y)
                if self.grid[(i,j)] == '*':
                    window.blit(im_wall, (x,y))
                #elif self.grid[(i,j)] == ' ':
                #    window.blit(im_floor, (x,y))
                #elif self.grid[(i,j)] == 'H':
                #    window.blit(im_tool, (x,y))
                elif self.grid[(i,j)] == 'X':
                    window.blit(im_gardien, (x,y))
                #elif self.grid[(i,j)] == 'S':
                #    window.blit(image_mac, (x,y))
        #pygame.display.flip()      

                
            





        
        
   


