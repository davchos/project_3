
import pygame
from pygame.locals import *
from Manager import Manager
from Personnage import Personnage
from Board import Board

if  __name__ == "__main__":
    mac = Personnage()
    board = Board()
    manager = Manager(mac, board)
    manager.play()