"""
code to launch the game
"""

from manager import Manager
from character import Personnage
from board import Board

if  __name__ == "__main__":
    Manager(Personnage(), Board()).play()
