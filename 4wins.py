class Player(object):
    def __init__(self):
        self._name = raw_input("Player name: ")
        while True:
            self._symbol = raw_input("Symbol (1 Character): ")
            if len(self._symbol) == 1 and self._symbol != "":
                break
            else:
                print "Only symbol with 1 character allowed."
    
    def get_name(self):
        return self._name        
    
    def get_symbol(self):
        return self._symbol
        

class Field(object):
    def __init__(self,height=3,width=3,wins=3):
        self._height = height
        self._width = width
        self._wins = wins
        self._pos = [[" " for i in xrange(self._width)] for k in xrange(self._height)]
        
        self._possibilities1 = []
        wins = self._wins
        needed = wins - 1
        for j in xrange(self._width-needed):
            for i in xrange(self._height-needed):
                self._possibilities1.append([(needed-k+i,j+k) for k in xrange(wins)])
                
        self._possibilities2 = []
        wins = self._wins
        needed = wins - 1
        for j in xrange(self._width-needed):
            for i in xrange(self._height-needed):
                self._possibilities2.append([(i+k,j+k) for k in xrange(wins)])
        
    def __str__(self):
        m = self._pos
        grid = ""
        for i in xrange(self._height):
            grid += "| "
            for j in xrange(self._width):
                grid += " " + m[i][j] + " | "
            grid += "\n"
            grid += "|____"*self._width + "|\n"
        nr_col = range(1,self._width+1)
        bottom = []
        for nr in nr_col:
            if nr < 10:
                bottom.append("|_0{}_".format(nr))
            else:
                bottom.append("|_{}_".format(nr))
        for b in bottom:
            grid += b
        grid += "|"
        return grid
        
    def fill(self, col, player):
        while True:
            bound = [i for i in xrange(1,self._width+1)]
            if int(col) in bound:
                break
            else:
                print "Invalid input for row or column! Valid are 1 to 7."
                col = raw_input("Column: ")
                      
        cond = True
        while cond:
            for row in [self._height-i-1 for i in xrange(self._height)]:
                if self._pos[row][int(col)-1] == " ":
                    self._pos[row][int(col)-1] = player.get_symbol() 
                    return False
            else:
                print "Column already full."
                col = raw_input("Column: ")
                cond = self.fill(col,player)
        
    def clear_field(self):
        self._pos = [[" " for i in xrange(self._width)] for k in xrange(self._height)]
    
    def check_row(self):
        for row in xrange(self._height):
            count = 1
            for col in xrange(self._width-1):
                if self._pos[row][col] == self._pos[row][col+1] and self._pos[row][col] != " ":
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 1
        
        return False
        
    def check_column(self):
        for col in xrange(self._width):
            count = 1
            for row in xrange(self._height-1):
                if self._pos[row][col] == self._pos[row+1][col] and self._pos[row][col] != " ":
                    count += 1
                    if count == self._wins:
                        return True
                else:
                    count = 1
        
        return False
    
    def check_diagonals1(self):
        for pos in self._possibilities1:
            sym = self._pos[pos[0][0]][pos[0][1]]
            for (i,j) in pos:
                if self._pos[i][j] == " " or self._pos[i][j] != sym:
                    break
            else:
                return True
                
        return False           
                
    
    def check_diagonals2(self):        
        for pos in self._possibilities2:
            sym = self._pos[pos[0][0]][pos[0][1]]
            for (i,j) in pos:
                if self._pos[i][j] == " " or self._pos[i][j] != sym:
                    break
            else:
                return True
                
        return False
        
    def check_all(self):
        if self.check_column() or self.check_row() or self.check_diagonals1() or self.check_diagonals2():
            return True
        else:
            return False


class Game(Field,Player):
    def __init__(self,height=6,width=7,wins=4):
        self._field = Field(height,width,wins)
      
    def start(self):
        replay = True
        new = True
        while replay:
            self._field.clear_field()
            if new:
                self.set_players()
            else:
                self._p1, self._p2 = self._p2, self._p1
            for i in xrange(self._field._width*self._field._height):
                if i%2 == 0:
                    win = self.turn(self._p1)
                    if win:
                        print self._field
                        print "\n\n" + self._p1.get_name() + " HAS WON!"
                        break
                else:
                    win = self.turn(self._p2)
                    if win:
                        print self._field
                        print "\n\n" + self._p2.get_name() + " HAS WON!"
                        break
            else:
                print self._field
                print "\n\n It's a tie!"
                
            ans = raw_input("Want to have a rematch [y/n]? ").lower()
            if ans == "n" or ans == "no" or ans == "nein":
                replay = False
            if replay:
                ans = raw_input("New players [y/n]? ").lower()
                if ans == "n" or ans == "no" or ans == "nein":
                    new = False
                else:
                    new = True
            else:
                print "Good bye!"
                
    def set_players(self):
        cond = True
        while cond:
            self._p1 = Player()
            self._p2 = Player()
            if self._p1.get_name() != self._p2.get_name() and self._p1.get_symbol() != self._p2.get_symbol():
                break
            print "Names and Symbols of the players have to be different!"
            
    def turn(self,player):
        print "\n\n", self._field
        print "\n" + player.get_name() + " has to play."
        while True:
            loc = raw_input("Column: ")
            if loc == "exit":
                return True
            if len(loc) == 1:
                try:
                    self._field.fill(int(loc),player)
                except ValueError:
                    print "Invalid input. Allowed is 'column(integer)'."
                    continue
                else:
                    break
            else:
                print "Input with one integer needed!"
                continue
        if self._field.check_all():
            print "\n\n\n{} has won!".format(player.get_name())
            return True
        else:
            return False
            
#•In Brackets you can choose width, height, wins
Game = Game(6,7,4)
Game.start()