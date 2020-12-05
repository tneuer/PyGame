import re
import os
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from FireClass import Fire
from SetClass import SET

lbox = []
invalidator = []
validator = []
totalshipnumber = 2 #2:Battleship,3:Destroyer,4:Cruiser,5:Submarines

class Help():
    @classmethod
    def helpwindow(cls,nr):
        root = Tk()
        root.geometry('0x0-1+1')
        messagebox.showinfo(message=cls.help(nr))
        root.destroy()
        
    
    @staticmethod
    def help(nr):
        if nr == 1:
            return("\n\nEach player gets a fleet of 10 ships: \n\n" \
                 + "1x Battleship of length 5 \n" \
                 + "2x Destroyer of length 4 \n" \
                 + "3x Cruiser of length 3 \n" \
                 + "4x Submarine of length 2 \n" \
                 + "\n" \
                 + "Ships are not allowed to touch other ships, also not in a corner. \n" \
                 + "This will be marked by an '*'(red) during the set up of your fleet. \n" \
                 + "Undamaged ships are marked as '@'(green). \n" \
                 + "Hit ship parts are marked with 'X'(Red). \n" \
                 + "Hits in the water are marked with '~'(Blue). \n\n" \
                 + "During SETUP: Left mouseclick-Start Position, right mouseclick-End Position/Orientation. \n" \
                 + "\n" \
                 + "During Target Selection: Left mouseclick-Select Position. \n" \
                 + "\n" \
                 + "Keep two commands in mind that are always available, except for name selection inputs: \n\n\n" \
                 + "HELP: Shows you a short advice what you are supposed to do. Furthermore it displays all available commands." \
                 + "\n\n" \
                 + "EXIT: Fails the program on purpose to exit the game.\n\n"\
                 + "ATTENTION: While the music selection window is open, the game is paused!")

        elif nr == 2:
            return("\n Advice: Choose a position to shoot at, for example A1 or j6.\n" \
                 + "Select a position with a left mouseclick.\n\n" \
                 + "Undamaged ships are marked as '@'. \n" \
                 + "Hit ship parts are marked with 'X'(Red). \n" \
                 + "Hits in the water are marked with '~'(Blue). \n\n" \
                 + "Two Fields are shown. Your own above and below the field to shoot at.\n\n" \
                 + "Following commands are available: \n\n" \
                 + "Help - You already used it to get here.\n" \
                 + "Exit - Leave the game.\n" \
                 + "Select Sound - Change music or get a new soundtrack.\n" \
                 + "Damage Report - Shows the position of our fleet and there status.\n" \
                 + "Change Name - Changes Name of your Battleship. \n")

        elif nr == 3:
            return("\n Advice: Choose a postion for your ship. Allowed are only horizontal and vertical lines.\n" \
                 + "ATTENTION: Left mouse click for Start position, right mouse click for End Position/Orientation. \n" \
                 + "The input format is 'LetterDigit LetterDigit', for example f6 f9 for a ship of length 4.\n"\
                 + "'*'(Red) marks invalid positions, '@'(green) marks ships that are already set.\n" \
                 + "If you are unhappy with a chosen position, don't worry.\n" \
                 + "You have the option to change the position once your whole fleet is set.\n" \
                 + "Changing the name of your Battleship is possible after you set your fleet.\n\n" \
                 + "Following commands are available: \n\n" \
                 + "Help - You already used it to get here.\n" \
                 + "Exit - Leave the game.\n" \
                 + "Select Sound - Change music or get a new soundtrack.\n")
       
        elif nr == 4:
            return("\n Advice: Choose the name of the ship you want to delete, the names are shown above the input.\n" \
                 + "'None' if you are finished deleting ships. \n" \
                 + "'*'(Red) marks invalid positions, '@'(green) marks ships that are already set.\n" \
                 + "Changing the name of your Battleship is possible after you set your fleet.\n\n" \
                 + "Following commands are available: \n\n" \
                 + "Help - You already used it to get here.\n" \
                 + "Exit - Leave the game.\n" \
                 + "Select Sound - Change music or get a new soundtrack.\n")
        
        elif nr == 5:
           return("\n Advice: Press 'n' if you want to change one or more ship positions.\n" \
                 + "'*'(Red) marks invalid positions, '@'(green) marks ships that are already set.\n" \
                 + "Changing the name of your Battleship is possible after you set your fleet.\n\n" \
                 + "Following commands are available: \n\n" \
                 + "Help - You already used it to get here.\n" \
                 + "Exit - Leave the game.\n" \
                 + "Select Sound - Change music or get a new soundtrack.\n")
                 
        elif nr == 6:
            return("\n Advice: Press 'n' to select specific ships you want to delete, press 'y' to reset the whole fleet.\n" \
                 + "'*'(Red) marks invalid positions, '@'(green) marks ships that are already set.\n" \
                 + "Changing the name of your Battleship is possible after you set your fleet.\n\n" \
                 + "Following commands are available: \n\n" \
                 + "Help - You already used it to get here.\n" \
                 + "Exit - Leave the game.\n" \
                 + "Select Sound - Change music or get a new soundtrack.\n")

            
            
            
class Soundtracks():
    songs = {0: 'No music', \
             1: 'Pirates of the Carribean Soundtrack', \
             2: 'Lord of the Rings Soundtrack', \
             3: 'Requiem for a Dream', \
             4: 'One Piece Karakuri Defence', \
             5: 'One Piece Fight Music', \
             6: 'Star Wars: Fall to the Dark Side', \
             7: 'Conquest of Paradise', \
             8: 'Ride of the Valkyries' }
    
    @staticmethod
    def window():
        global lbox        
        root = Tk()
        root.title("Music selection")
        frame = ttk.Frame(root, padding = (5,5,12,12))
        frame.grid(column = 0, row = 0, sticky= (N,W,S,E))
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
        root.minsize(300,100)
        root.geometry('500x300-50+100')
        
        sn = [i for i in Soundtracks.songs.values()]
        songnames = StringVar(value=sn)
        
        lbox = Listbox(frame, listvariable = songnames, width=10)
        lbox.selection_set(0)
        play = ttk.Button(frame, text = "Play", command = Soundtracks.playsong)
        continueB = ttk.Button(frame, text = "Continue", command = root.destroy, default = 'active')
        
        lbox.grid(column=0,row=0,rowspan=5,sticky=(N,S,E,W))
        play.grid(column=2, row=3)
        continueB.grid(column=2,row=4)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        
        lbox.bind('<Double-1>', Soundtracks.playsong)
        root.bind('<Return>', root.destroy)
        
        # Colorize alternating lines of the listbox
        for i in range(0,len(sn),2):
            lbox.itemconfigure(i, background='#f0f0ff')
        
        root.mainloop()
                 
    @staticmethod
    def playsong(*args):
        nr = lbox.curselection()
        if len(nr) == 1:
            nr = int(nr[0])
            if nr == 1:
                if os.path.isfile("C:/Users/Spider Schwein/Desktop/PyGame/Battleships/PiratesCarribean.mp3"):
                    os.system("start PiratesCarribean.mp3")
                else:
                    webbrowser.open("https://www.youtube.com/watch?v=MwOdT4SmxTA")
        
            elif nr == 2:
                if os.path.isfile("C:/Users/Spider Schwein/Desktop/PyGame/Battleships/HerrDerRinge.mp3"):
                    os.system("start HerrDerRinge.mp3")
                else:
                    webbrowser.open("https://www.youtube.com/watch?v=wshFonw_TEE")
           
            elif nr == 3:
                if os.path.isfile("C:/Users/Spider Schwein/Desktop/PyGame/Battleships/RequiemForADream.mp3"):
                    os.system("start RequiemForADream.mp3")
                else:
                    webbrowser.open("https://www.youtube.com/watch?v=iYAaN9EMpE0&t=5s")
        
            elif nr == 4:
                if os.path.isfile("C:/Users/Spider Schwein/Desktop/PyGame/Battleships/OnePieceKarakuri.mp3"):
                    os.system("start OnePieceKarakuri.mp3")
                else:
                    webbrowser.open("https://www.youtube.com/watch?v=Gn5idEi7gtc&t=22s")
        
            elif nr == 5:
                if os.path.isfile("C:/Users/Spider Schwein/Desktop/PyGame/Battleships/OnePieceFight.mp3"):
                    os.system("start OnePieceFight.mp3")
                else:
                    webbrowser.open("https://www.youtube.com/watch?v=3P7Ee85Z32Y")
          
            elif nr == 6:
                if os.path.isfile("C:/Users/Spider Schwein/Desktop/PyGame/Battleships/DarkSide.mp3"):
                    os.system("start DarkSide.mp3")
                else:
                    webbrowser.open("https://www.youtube.com/watch?v=nHNbXfbjI2k")          

            elif nr == 7:
                if os.path.isfile("C:/Users/Spider Schwein/Desktop/PyGame/Battleships/ConquestOfParadise.mp3"):
                    os.system("start ConquestOfParadise.mp3")
                else:
                    webbrowser.open("https://www.youtube.com/watch?v=WYeDsa4Tw0c")
            
            elif nr == 8:
                if os.path.isfile("C:/Users/Spider Schwein/Desktop/PyGame/Battleships/Valkyries.mp3"):
                    os.system("start Valkyries.mp3")
                else:
                    webbrowser.open("https://www.youtube.com/watch?v=AFa1-kciCb4")


                    
class Player(object):
    def __init__(self):
        while True:
            self._name = input("Player name: ")
            if re.search(r'^\s+', self._name) or self._name == "":
                print("Empty space not allowed as name or beginning of a name.")
            else:
                break
        self._fleet = Fleet()     
        self._own_sea = self._fleet._ocean
        self._enemy_sea = Field()        

    def get_name(self):
        return self._name

        
        
class Field(object):
    """
    Methods:
        __init__ : Creates empty positions
        __str__ : Designs the field
        clear_field: erases all positions that are not empty
        fill: fills a field position with a certain symbol
        mark_invalid: all surroundings of a ship are invalid positions for the next ship, gets marked with '*'
        prepapare: erases the '*' from the mark_invalid method
    """
    letters = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
    revletters = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J"}
    
    def __init__(self):
        self._height = 10
        self._width = 10
        self._letters = sorted(Field.letters.keys())
        self._pos = [[" " for i in range(self._width)] for k in range(self._height)]

    def __str__(self):
        m = self._pos
        grid = ""
        nr_col = range(1, self._width+1)
        top = ["__" + "_____"*self._width + "_____\n|__"]
        for nr in nr_col:
            if nr < 10:
                top.append("|_0{}_".format(nr))
            else:
                top.append("|_{}_".format(nr))
        top += ["|__|\n"]
        for t in top:
            grid += t
        for i, letter in zip(range(self._height), self._letters):
            grid += "|  " + "|    " * self._width + "|  |\n"
            grid += "|{} | ".format(letter)
            for j in range(self._width):
                grid += " " + m[i][j] + " | "
            grid += "{}|\n|__".format(letter)
            grid += "|____"*self._width + "|__|\n"
        bottom = ["|__"]
        for nr in nr_col:
            if nr < 10:
                bottom.append("|_0{}_".format(nr))
            else:
                bottom.append("|_{}_".format(nr))
        bottom += ["|__|"]
        for b in bottom:
            grid += b
        return grid

    def clear_field(self):
        self._pos = [[" " for i in range(self._width)] for k in range(self._height)]

    def fill(self, all_pos, sym):
        for pos in all_pos:
            self._pos[pos[0]-1][pos[1]-1] = sym

    def mark_invalid(self, all_pos):
        global invalidator
        invalidator = []
        self.mark_valid(all_pos)
        for pos in all_pos:
            x = pos[0]
            y = pos[1]
            surrounding = [(x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y)]
            for point in surrounding:
                if 0 < point[0] < 11 and 0 < point[1] < 11:
                    if self._pos[point[0]-1][point[1]-1] == " ":
                        self.fill([point], "*")
                        invalidator.append(point)
        
        return invalidator
    
    def mark_valid(self, all_pos):
        global validator
        validator = []
        for pos in all_pos:
            x = pos[0]
            y = pos[1]
            surrounding = [(x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y)]
            for point in surrounding:
                if 0 < point[0] < 11 and 0 < point[1] < 11:
                    if self._pos[point[0]-1][point[1]-1] == "*":
                        self.fill([point], " ")
                        validator.append(point)
        return validator
        
    def prepare(self):
        """
        Clears field of '*' symbols after setup.
        """
        for i in range(self._width):
            for j in range(self._height):
                if self._pos[i][j] != Ship.symbol:
                    self._pos[i][j] = " "
        
    def check_for_survivors(self):
        """
        Returns True if the game has to continue, False if there is a winner.
        """
        for i in range(self._width):
            for j in range(self._height):
                if self._pos[i][j] == Ship.symbol:
                    return True
        else:
            return False

            
            
class Ship(object):
    kind,desnr,crunr,subnr = ["Battleship","Destroyer","Cruiser","Submarine"],1,1,1
    symbol = "@"
    def __init__(self,name,posi,sur):
        self._state = 0 #Number of hit parts
        if name == Ship.kind[0]:
            self._name = input("Special name for your Battleship: ")
            if not self._name:
                self._name = "Battleship"
            self._length = 5
        elif name == Ship.kind[1]:
            self._name = name + str(Ship.desnr)
            Ship.desnr += 1
            self._length = 4           
        elif name == Ship.kind[2]:
            self._name = name + str(Ship.crunr)
            Ship.crunr += 1
            self._length = 3
        elif name == Ship.kind[3]:
            self._name = name + str(Ship.subnr)
            Ship.subnr += 1
            self._length = 2
        while True:
            input("Press ENTER to set your {} of length {}".format(self._name,self._length))
            self._pos = SET(self._name,self._length,posi,sur)
            self._pos = self._pos.pos            
            if self._pos == "exit":
                raise Exception("Good bye!")
            elif self._pos.lower() == "help" or self._pos == "":
                Help.helpwindow(3)
                continue
            elif self._pos.lower() == "select sound":
                print("Game is paused, to continue close music selection window.")
                Soundtracks.window()
                continue           
            elif self.validate_pos():
                self._pos = self.validate_pos()
                break
            
    def __str__(self):
        if self.get_state() == 0:
            state = "undamaged"
        elif self.get_state() < self.get_length():
            state = "damaged"
        else:
            state = "sunk"
        sl, sd, el, ed = self.get_pos()
        return "{} {}: {} parts hit. Position: {}{}-{}{}".format(self.get_name(),state, self.get_state(),sl,sd,el,ed)
    
    def validate_pos(self):
        pos = self._pos
        pattern = r"([a-jA-J]((10)|([1-9])))\s([a-jA-J]((10)|([1-9])))"        
        match = re.search(pattern,pos)
        if match:
            match = [match.groups()[0], match.groups()[4]]
            if match[0] == match[1]:
                print("Please give an orientation.")
                return False
            sl, sd, el, ed = match[0][0].upper(), int(match[0][1:]), match[1][0].upper(), int(match[1][1:])   
        else:
            print("Input format: Start(Letter[A-J]Digit[1-10]) End(LetterDigit), example: A1 A5.")
            return False
        dic = Field.letters
        revdic = Field.revletters
        if sl!=el and sd!=ed:
            print("Ship has to be in a straight horizontal or vertical line.")
            return False
        else:
            if sd == ed:
                if dic[sl] > dic[el]:
                    if (dic[sl]-self._length+1 < 1):
                        print("Out of bounds!")
                        return False                     
                    end = "{}{}".format(revdic[dic[sl]-self._length+1],sd)
                else:
                    if (dic[sl]+self._length-1 > 10):
                        print("Out of bounds!")
                        return False
                    end = "{}{}".format(revdic[dic[sl]+self._length-1],ed)
            else:
                if sd > ed:
                    if (sd-self._length+1 < 1):
                        print("Out of bounds!")
                        return False
                    end = "{}{}".format(sl,sd-self._length+1)
                else:
                    if (sd+self._length-1 > 10):
                        print("Out of bounds!")
                        return False
                    end = "{}{}".format(sl,sd+self._length-1)
                
            return match[0]+" "+end
        
    def get_name(self):
        return self._name
        
    def get_length(self):
        return self._length
        
    def get_state(self):
        return self._state
       
    def get_pos(self):
        """
        returns the input position but split up in tuple with (StartLetter,StartDigit,EndLetter,EndDigit)
        """
        pos = self._pos.split()
        return (pos[0][0].upper(), int(pos[0][1:]), pos[1][0].upper(), int(pos[1][1:]))       

    def _internal_pos(self):
        """
        returns a list of tupels with all the positions of the ship, not just start and end point.
        """
        sl, sd, el, ed = self.get_pos()
        dic = Field.letters
        if sl == el:
            if ed < sd:
                sd, ed = ed, sd
            return [(dic[sl],i) for i in range(sd,ed+1)]
        if sd == ed:
            if el < sl:
                sl, el = el, sl
                
            return [(i,sd) for i in range(dic[sl],dic[el]+1)]
    
    @staticmethod
    def delete(name, ocean, fleet, deletenr):
        """
        Erases a ship with 'name' off the field and the fleet it was part off.
        """
        count=0
        for ship in fleet:
            if name == ship.get_name():
                pos = ship._internal_pos()
                ocean.mark_valid(pos)
                for point in pos:
                    ocean._pos[point[0]-1][point[1]-1] = " " 
                del fleet[count]
                if len(pos) == 5:
                    deletenr[0] += 1
                    return [deletenr[0],"B"]
                else:
                    deletenr[0] += 1
                    return [deletenr[0], " "]
                break
            count += 1
        else:
            print("Invalid name!")
            return False
        
 
            
class Fleet(object):
    def __init__(self):
        self._ocean = Field()
        self._fleet = self.create_fleet()
    
    def __str__(self):
        fleet = ""
        for ship in self._fleet:
            fleet += str(ship) + "\n"
        return fleet
        
    def create_fleet(self):
        fleet = []
        totposi = []
        global invalidator
        global validator
        invalidator = []
        validator = []
        for ship in [Ship.kind[i-1] for i in range(1,totalshipnumber) for j in range(i)]:
            error = ""
            while True:
                print(self._ocean)
                print("\n_______" + error)    
                boat = Ship(ship, totposi, invalidator)
                valid = self.check_new_positions(fleet,boat)
                if valid[0]:
                    fleet.append(boat)
                    self._ocean.fill(boat._internal_pos(),Ship.symbol)
                    totposi = Fleet.get_all_pos(fleet)
                    self._ocean.mark_invalid(totposi)
                    break
                else:
                    error = valid[1]
        self._ocean.prepare()
        print(self._ocean)
        while True:
            ans = input("Are you happy with your fleet? [y/n]: ").lower()
            if ans.lower() == "help" or ans == "":
                Help.helpwindow(5)
                continue
            elif ans == "exit":
                raise Exception("Good bye!")
            elif ans.lower() == "select sound":
                print("Game is paused, to continue close music selection window.")
                Soundtracks.window()
                continue
            elif ans in ["n", "no", "nein", "nope"]:
                ans = input("Do you want to reset the whole fleet? [y/n]: ").lower()
                if ans.lower() == "help" or ans == "":
                    Help.helpwindow(6)
                    continue
                elif ans == "exit":
                    raise Exception("Good bye!")
                elif ans.lower() == "select sound":
                    print("Game is paused, to continue close music selection window.")
                    Soundtracks.window()
                    continue
                elif ans in ["yes", "y", "jap", "ja"]:
                    self._ocean.clear_field()
                    self.create_fleet()
                else:
                    deleted = []
                    deletenr = [0," "]
                    while True:
                        print("\n")
                        for ship in fleet:
                            print(ship)
                        ans = input("Which ship do you want to delete [name,None]? ")
                        if ans == "None":
                            break
                        elif ans.lower() == "help" or ans == "":
                            Help.helpwindow(4)
                            continue
                        elif ans == "exit":
                            raise Exception("Good bye!")
                        elif ans.lower() == "select sound":
                            print("Game is paused, to continue close music selection window.")
                            Soundtracks.window()
                            continue       
                        else:
                            deletenr = Ship.delete(ans, self._ocean,fleet,deletenr)
                            if str(deletenr) != "False":
                                print(self._ocean)
                                if deletenr[1] == "B":
                                    ans = "Battleship"
                                    deleted += [(ans, 0)]
                                else:
                                    ans = re.search("[a-zA-Z]+",ans).group()
                                    deleted += [(ans, deletenr[0])]
                    self._ocean.mark_invalid(self.get_all_pos(fleet))
                    sort = {}
                    for i in deleted:
                        sort["{}".format(i[1])] = i
                    keyssorted = sorted(sort.keys())
                    deleted = [sort[key] for key in keyssorted]
                    totposi = Fleet.get_all_pos(fleet)
                    for new in deleted:
                        while True:
                            print(self._ocean)
                            listpos = new[1]
                            fleet.insert(listpos, Ship(new[0],totposi,invalidator))
                            try:
                                fleet[listpos]
                            except IndexError:
                                listpos = len(fleet) - 1
                            valid = self.check_new_positions(fleet,fleet[listpos])
                            if valid[0]:
                                self._ocean.fill(fleet[listpos]._internal_pos(), Ship.symbol)
                                self._ocean.mark_invalid(fleet[listpos]._internal_pos())
                                totposi = Fleet.get_all_pos(fleet)
                                invalidator = self._ocean.mark_invalid(totposi)
                                print(self._ocean)
                                break
                            else:
                                error = valid[1]
                                del fleet[listpos]
                    self._ocean.prepare()
                    print(self._ocean)  
            else:
                break
        return fleet

    def check_new_positions(self, fleet, boat):
        boat_pos = boat._internal_pos()
        rev = Field.revletters
        for pos in boat_pos:
            if self._ocean._pos[pos[0]-1][pos[1]-1] != " ":
                print("Position '{}{}' not availabale.".format(rev[pos[0]], pos[1]))
                return (False, "Position '{}{}' not availabale.".format(rev[pos[0]], pos[1]))

        return (True, "")

    @staticmethod
    def get_all_pos(fleet=[]):
        tot_pos = []
        for ship in fleet:
            tot_pos += ship._internal_pos()
        return tot_pos

    def update_damage(self, pos):
        for ship in self._fleet:
            if pos in ship._internal_pos():
                ship._state += 1
                break

            
 
class Game(object):

    def start(self):
        replay = True
        while replay:
            Help.helpwindow(1)
            print("Game is paused, to continue close music selection window.")
            Soundtracks.window()
            self.set_players()
            for i in range(200):  # 200 shots is maximum, then all fields are filled.
                if i % 2 == 0:
                    win = self.turn(self._p1, self._p2)
                    if win:
                        print(self._p1._own_sea)
                        print(self._p1._enemy_sea)
                        print("\n\n" + self._p1.get_name() + " HAS WON!")
                        break
                else:
                    win = self.turn(self._p2, self._p1)
                    if win:
                        print(self._p2._own_sea)
                        print(self._p2._enemy_sea)
                        print("\n\n" + self._p2.get_name() + " HAS WON!")
                        break
                input("If next player is ready, press ENTER: ")
            ans = input("Want to have a rematch [y/n]? ").lower()
            if ans == "n" or ans == "no" or ans == "nein":
                replay = False
                print("Good bye!")
      
    def set_players(self):
        cond = True
        while cond:
            self._p1 = Player()
            self._p2 = Player()
            if self._p1.get_name() != self._p2.get_name():
                break
            print("Names of the players have to be different!")
 
    def turn(self,player,enemy):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n_______OWN FIELD:", player._own_sea)
        print("\n\n_______Enemy's FIELD:", player._enemy_sea)
        print("\n" + player.get_name() + " has to choose a position to shoot at!")        
        input("Ready? [Enter] ")
        while True:
            hit = Fire(player.get_name(), player._enemy_sea._pos)
            hit = hit.pos
            if hit.lower() == "exit":
                return True
            if hit.lower() == "help" or hit == "":
                Help.helpwindow(2)
                continue
            elif hit.lower() == "select sound":
                print("Game is paused, to continue close music selection window.")
                Soundtracks.window()
                continue
            elif hit.lower() == "damage report":
                print("\n", player._fleet)
                input("Ready? [Enter] ")
                continue
            elif hit.lower() == "change name":
                new = input("New name: ")
                player._fleet._fleet[0]._name = new
                print("Your Battleship is now called {}.".format(new))
                input("Ready? [Enter] ")
                continue
            if Game.check_hit(hit):
                x, y = Game.check_hit(hit)
                if player._enemy_sea._pos[x-1][y-1] != " ":
                    print("You already have shot at this position. Choose a new one.")
                elif enemy._own_sea._pos[x-1][y-1] == " ":
                    rev = Field.revletters
                    print("Missed! There was no enemy ship at position {}{}.".format(rev[x], y))
                    player._enemy_sea.fill([(x, y)], "~")
                    enemy._own_sea.fill([(x, y)], "~")
                    break
                else:
                    print("Shot landed! You successfully attacked {}'s fleet!".format(enemy.get_name()))      
                    player._enemy_sea.fill([(x, y)], "X")
                    enemy._own_sea.fill([(x, y)], "X")
                    enemy._fleet.update_damage((x, y))
                    break

        if not enemy._own_sea.check_for_survivors():
            print("\n\n\n{} has won!".format(player.get_name()))
            return True
        else:
            return False

    def check_hit(self, pos):
        pattern1 = r"[a-jA-J][1-9]"
        pattern2 = r"[a-jA-J]10"
        match1 = re.search(pattern1, pos)
        match2 = re.search(pattern2, pos)  
        if match2:
            match = match2.group()
            x, y = match[0].upper(), int(match[1:])
        elif match1:
            match = match1.group()
            x, y = match[0].upper(), int(match[1])
        else:
            root = Tk()
            root.geometry('0x0-1+1')
            messagebox.showinfo(message="Input format: Start(Letter[A-J]Digit[1-10]), for example A1.")
            root.destroy()
            root.mainloop()
            
            print("Input format: Start(Letter[A-J]Digit[1-10]), for example A1.")
            return False
        dic = Field.letters
        x = dic[x]
        return (x,y)
     
        
Game = Game()
Game.start()