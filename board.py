"""
Class to manage the game play
"""
import random
import pygame
import numpy as np
from const import (
    nbcol, 
    nblig, 
    wall,
    startcol,
    startlig,
    taille_sprite,
    numberoftools,
    image_floor,
    image_gardien,
    image_mac,
    image_tool,
    image_wall
) 
#from pygame.locals import *


class Board(object):
    """ Class to manage game play """
    def __init__(self):
        self.explored = 0
        self.grid = np.full((nblig, nbcol), wall)
        self.tools = []
        self.path = []
        self.paths = []
        self.mac = []
        self.explore(startlig, startcol)
        self.save_paths()
        self.setup_tools()
        self.setup_personnage()

    def getdirection(self, plig, pcol):
        """ retrun all the possible directions possible from a given position """
        dirs = []
        if plig - 2 > 0:
            if self.grid[(plig-2, pcol)] == wall:
                dirs.append("up")
        if pcol + 2 < nbcol - 1:
            if self.grid[(plig, pcol+2)] == wall:
                dirs.append("right")
        if plig + 2 < nblig - 1:
            if self.grid[(plig+2, pcol)] == wall:
                dirs.append("down")
        if pcol - 2 > 0:
            if self.grid[(plig, pcol-2)] == wall:
                dirs.append("left")
        return dirs

    def digwall(self, plig, pcol):
        """ mark the cell as floor (" "), and add it to the path """
        self.grid[(plig, pcol)] = " "
        self.path.append([plig, pcol])

    def explore(self, plig, pcol):
        """
            Part of DFS algo, at the begining all cells are wall.
            Uses recursivity to visit randomly cells
        """
        self.digwall(plig, pcol)
        self.explored += 1
        while self.explored < (nblig * nbcol/2):
            dirs = self.getdirection(plig, pcol)
            if dirs:
                choice = random.randrange(len(dirs))
                temp_choice = dirs[choice]
                print("direction is %s", temp_choice)
                if temp_choice == "up":
                    self.digwall(plig-1, pcol)
                    self.explore(plig-2, pcol)
                if temp_choice == "right":
                    self.digwall(plig, pcol+1)
                    self.explore(plig, pcol+2)
                if temp_choice == "down":
                    self.digwall(plig+1, pcol)
                    self.explore(plig+2, pcol)
                if temp_choice == "left":
                    self.digwall(plig, pcol-1)
                    self.explore(plig, pcol-2)
            else:
                break

    def save_paths(self):
        """ Start from (startlig,startcol)
        save the branch of the tree as a [], and queue it in paths
        """
        last = 0
        for temp_0 in range(len(self.path)-1):
            if abs(self.path[temp_0][0] - self.path[temp_0+1][0]) > 1 \
               or abs(self.path[temp_0][1] - self.path[temp_0+1][1]) > 1:
                self.paths.append(self.path[last:temp_0+1])
                last = temp_0+1

    def setup_tools(self):
        """ place randomly the tools, Todo check the placement and nulber of tools"""
        for i in range(numberoftools):
            temp_0 = True
            while temp_0:
                temp_1 = random.randrange(1, len(self.paths))
                temp_2 = random.randrange(1, len(self.paths[temp_1]))
                if self.paths[temp_1][temp_2] not in self.tools \
                   and (temp_1 != 0 and temp_2 != 0) \
                   and (temp_1 != self.mac and temp_2 < len(self.paths[temp_1]) - 2):
                    self.grid[(self.paths[temp_1][temp_2][0], self.paths[temp_1][temp_2][1])] = "H"
                    self.tools.append((self.paths[temp_1][temp_2][0], \
                        self.paths[temp_1][temp_2][1]))
                    temp_0 = False

    def setup_personnage(self):
        """ place Mac and the bad guy on the board """
        self.grid[(self.paths[0][0][0], self.paths[0][0][1])] = "X"
        temp_1 = True
        while temp_1:
            for temp_2 in range(1, len(self.paths)):
                if len(self.paths[temp_2]) > 3:
                    self.grid[(self.paths[temp_2][-1][0], self.paths[temp_2][-1][1])] = "S"
                    self.mac = temp_2
                    temp_1 = False
                    break

    def init_board(self, window):
        """ This function blit the board on the window """
        self.im_wall = pygame.image.load(image_wall).convert()
        self.im_tool = pygame.image.load(image_tool).convert_alpha()
        self.im_gardien = pygame.image.load(image_gardien).convert_alpha()
        self.im_floor = pygame.image.load(image_floor).convert()
        self.im_mac = pygame.image.load(image_mac).convert_alpha()
        self.window = window

        for i in range(nblig):
            for j in range(nbcol):
                y_pos = i * taille_sprite
                x_pos = j * taille_sprite
                if self.grid[(i, j)] == '*':
                    window.blit(self.im_wall, (x_pos, y_pos))
                elif self.grid[(i, j)] == ' ':
                    window.blit(self.im_floor, (x_pos, y_pos))
                elif self.grid[(i, j)] == 'H':
                    window.blit(self.im_tool, (x_pos, y_pos))
                elif self.grid[(i, j)] == 'X':
                    window.blit(self.im_gardien, (x_pos, y_pos))
                elif self.grid[(i, j)] == 'S':
                    window.blit(self.im_mac, (x_pos, y_pos))
         