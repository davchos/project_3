
from getkey import getkey, keys

from Manager import Manager
from Personnage import Personnage
from Board import Board


if  __name__ == "__main__":
    game = Manager()
    print(game.mac.position)
    
    while True:
        game.getuserinput()
        game.display()

    











    


