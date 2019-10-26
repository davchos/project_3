

from getkey import getkey, keys

from  Personnage import Personnage

from  Board import Board


class Manager():
    def __init__(self):
        self.mac = Personnage()
        self.b = Board()
        self.mac.position[0] = self.b.paths[self.b.mac][-1][0]
        self.mac.position[1] = self.b.paths[self.b.mac][-1][1]
        self.step = [0,0]
        self.display()

    def getuserinput(self):
        temp = [0,0]
        d = getkey()
        if d == keys.UP:
            self.step[0]= -1
            self.step[1]= 0
        elif d == keys.DOWN:
            self.step[0]= 1
            self.step[1]= 0
        elif d == keys.LEFT:
            self.step[0]= 0
            self.step[1]= -1
        elif d == keys.RIGHT:
            self.step[0]= 0
            self.step[1]= 1 
        elif d == 'Q':
            self.save_game()
            exit()   
        else:
            return          
        temp[0] = self.mac.position[0] + self.step[0]
        temp[1] = self.mac.position[1] + self.step[1]  
        print(self.mac.position)
        print(temp)
        print(self.b.grid[(temp[0],temp[1])])

        """ if not on path return """
        if self.b.grid[(temp[0],temp[1])] == self.b.wall:
            return
        if self.b.grid[(temp[0],temp[1])] == 'H':
            self.b.grid[(temp[0], temp[1])] = 'S'
            self.b.grid[(self.mac.position[0], self.mac.position[1])] = ' '
            self.mac.position[0] = temp[0]
            self.mac.position[1] = temp[1]
            self.mac.bag += 1
            #self.tool.remove([temp[1],temp[0]])
           
        if temp  ==  self.b.paths[0][1] and self.mac.bag != 3:
            exit("Perdu")
        if temp  ==  self.b.paths[0][1] and self.mac.bag == 3:
            exit("You are a winnner")
        self.b.grid[(temp[0], temp[1])] = 'S'
        self.b.grid[(self.mac.position[0], self.mac.position[1])] = ' '
        self.mac.position[0] = temp[0]
        self.mac.position[1] = temp[1]
        
        

    def display(self):
        for i in range(self.b.nblig):
            for j in range(self.b.nbcol):
                print(self.b.grid[(i,j)], end='')
            print()  

    def save_game(self):
        pass             
