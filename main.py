"""
code to launch the game
"""

from manager import Manager
from personnage import Personnage
from board import Board

if  __name__ == "__main__":
    MAC = Personnage()
    BOARD = Board()
    MANAGER = Manager(MAC, BOARD)
    MANAGER.play()
