# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 23:31:14 2016

@author: Spider Schwein
"""
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
    def __init__(self):
        self._pos = [[" "," "," "],[" "," "," "],[" "," "," "]]
        
    def __str__(self):
        m = self._pos
        return m[0][0] + " | " + m[0][1] + " | " + m[0][2] + "\n" + \
                "__|___|__ \n" + \
                m[1][0] + " | " + m[1][1] + " | " + m[1][2] + "\n" + \
                "__|___|__ \n" + \
                m[2][0] + " | " + m[2][1] + " | " + m[2][2] + "\n" + \
                "  |   |  \n"
        
    def fill(self, row, col, player):
        while True:
            bound = [1,2,3]
            if int(row) in bound and int(col) in bound:
                break
            else:
                print "Invalid input for row or column! Valid are 1,2 or 3."
                row, col = raw_input("Row Column: ").split()
                      
        cond = True
        while cond:
            if self._pos[int(row)-1][int(col)-1] == " ":
                self._pos[int(row)-1][int(col)-1] = player.get_symbol() 
                return False
            else:
                print "Field already taken."
                row, col = raw_input("Row Column: ").split()
                cond = self.fill(row,col,player)
        
    def clear_field(self):
        self._pos = [[" "," "," "],[" "," "," "],[" "," "," "]]
    
    def check_row(self):
        for row in xrange(3):
            for col in xrange(1,3):
                if self._pos[row][0] != self._pos[row][col] or self._pos[row][0] == " " :
                    break
            else:
                return True 
          
        return False
        
    def check_column(self):
        for col in xrange(3):
            for row in xrange(1,3):
                if self._pos[0][col] != self._pos[row][col] or self._pos[0][col] == " " :
                    break
            else:
                return True
        
        return False
    
    def check_diagonals1(self):
        for d in xrange(1,3):
            if self._pos[0][0] != self._pos[d][d] or self._pos[d][d] == " " :
                    break
        else:
            return True
        
        return False
    
    def check_diagonals2(self):
        for d in xrange(1,3):
            if self._pos[0][2] != self._pos[0+d][2-d] or self._pos[0][2] == " " :
                    break
        else:
            return True
        
        return False
    
    def check_all(self):
        if self.check_column() or self.check_row() or self.check_diagonals1() or self.check_diagonals2():
            return True
        else:
            return False


class TicTacToe(Field,Player):
    def __init__(self):
        self._field = Field()
    
    @property    
    def start(self):
        replay = True
        new = True
        while replay:
            self._field.clear_field()
            if new:
                self.set_players()
            else:
                self._p1, self._p2 = self._p2, self._p1
            for i in xrange(9):
                if i%2 == 0:
                    win = self.turn(self._p1)
                    if win:
                        print self._field
                        break
                else:
                    win = self.turn(self._p2)
                    if win:
                        print self._field
                        break
            else:
                print "It's a tie!"
                
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
        print player.get_name() + " has to play."
        while True:
            loc = raw_input("Row Column: ").split()
            if loc == ["exit"]:
                return True
            if len(loc) == 2:
                try:
                    self._field.fill(int(loc[0]),int(loc[1]),player)
                except ValueError:
                    print "Invalid input. Allowed is 'row(integer) column(integer)'."
                    continue
                else:
                    break
            else:
                print "Input with two integers needed!"
                continue
        if self._field.check_all():
            print "\n\n\n{} has won!".format(player.get_name())
            return True
        else:
            return False
          
T = TicTacToe()
T.start