
from getkey import getkey, keys

from Manager import Manager



if  __name__ == "__main__":
    game = Manager()
    print(game.mac.position)
    
    while True:
        game.getuserinput()
        game.display()

    











    


