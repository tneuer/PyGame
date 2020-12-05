from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import sample
import re
import time

class Minesweeper(object):
    def __init__(self):
        root = Tk()
        root.geometry('500x500+200+100')
        for i in range(3):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)
        
        difficulty = StringVar(value="Easy")
        
        new_start_B = ttk.Button(root, text = "New start")
        help_B = ttk.Button(root, text = "Help")
        difficulty_B = ttk.Combobox(root, textvariable = difficulty)
        difficulty_B['values'] = ('Easy','Medium','Hard','Customize')
        difficulty_B.state(['readonly']) 
        
        starter = lambda p: Minesweeper.start(difficulty.get(),root)
        new_start_B.bind('<1>', starter)
        help_B.bind('<1>', Minesweeper.helper)
        
        help_B.grid(row=0,column=0)
        new_start_B.grid(row=0,column=1)
        difficulty_B.grid(row=0,column=2)
        
        root.mainloop()
        
    @staticmethod
    def start(diff,root):
        global bombpositions
        root.destroy()
        if diff == "Easy":
            rows, columns, bombs = 8, 8, 10
            
        elif diff == "Medium":
            rows, columns, bombs = 16, 16, 40
            
        elif diff == "Hard":
            rows, columns, bombs = 16, 30, 99
        
        else:
            print(diff)
            rows = int(input("Rows: "))
            columns = int(input("Columns: "))
            bombs = int(input("Bombs: "))
            
        Minesweeper.create_window(rows, columns, bombs)
        bombpositions = Minesweeper.place_bombs(bombs)
        Minesweeper.count_neighbours(bombpositions, rows, columns)
        Minesweeper.set_Field()    
                      
    @staticmethod
    def create_window(rows, columns, bombs):
        global allFields
        global time_L
        global start_time
        start_time = time.clock()
        
        root = Tk()
        root.geometry('1200x600+20+20')
        
        if columns == 8:
            difficulty = StringVar(value="Easy")
        elif columns == 16:
            difficulty = StringVar(value="Medium")
        elif columns == 30:
            difficulty = StringVar(value="Hard")
        else:
            difficulty = StringVar(value = "{} {} {}".format(rows,columns,bombs))
            
        frame = ttk.Frame(root)
        new_start_B = ttk.Button(root, text = "New start")
        help_B = ttk.Button(root, text = "Help")
        count_L = ttk.Label(root, text = "0")
        time_L = ttk.Label(root, text = 0)
        difficulty_B = ttk.Combobox(root, textvariable = difficulty)
        difficulty_B['values'] = ('Easy','Medium','Hard', 'Customize')
        difficulty_B.state(['readonly'])
        
        starter = lambda p: Minesweeper.start(difficulty.get(),root)
        new_start_B.bind('<1>', starter)
        help_B.bind('<1>', Minesweeper.helper)
        
        frame.grid(row=1,column=0,rowspan=rows-1,columnspan=columns, sticky = (N,E,S,W))
        help_B.grid(row=0,column=0)
        count_L.grid(row=0,column=1)
        new_start_B.grid(row=0,column=2)
        time_L.grid(row=0,column=rows-2)        
        difficulty_B.grid(row=0,column=rows-1)
        
        for row in range(2):
            root.grid_rowconfigure(row, weight=(1+row)*100)
        for col in range(5):
            root.grid_columnconfigure(col, weight=1+col)
        
        for row in range(rows):
            frame.grid_rowconfigure(row, weight=1)
        for col in range(columns):
            frame.grid_columnconfigure(col, weight=1)
            
        allFields = {}
        reveal = lambda x: (lambda p: Minesweeper.revealer(x,rows,columns))
        mark = lambda x: (lambda p: Minesweeper.marker(x,count_L,bombs))
        question = lambda x: (lambda p: Minesweeper.questioner(x,count_L,bombs))
        
        count = 0
        for row in range(rows):
            for column in range(columns):
                lbl = Label(frame, text = "0", height=1, width=2)
                allFields["{}".format(count)] = lbl
                lbl.grid(row=row+1,column=column)
                lbl.bind('<1>', reveal(lbl))
                lbl.bind('<3>', mark(lbl))
                lbl.bind('<Double-3>', question(lbl))
                count += 1
            
        ttk.Sizegrip().grid(row=row+1,column=column+1,sticky=(S,E))
        return allFields
    
    @staticmethod
    def place_bombs(nrbombs):
        samplespace = [int(i) for i in allFields.keys()]
        bombpos = sample(samplespace,nrbombs)
        for pos in bombpos:
            allFields["{}".format(pos)].configure(bg = "red", text = "B")
                
        return bombpos
    
    def count_neighbours(bombpos, rows, cols):
        for pos in bombpos:
            sur = Minesweeper.find_surroundings(pos,rows,cols)
            
            for surpos in sur:
                entry = allFields["{}".format(surpos)]["text"]
                if entry == "B":
                    continue
                else:
                    allFields["{}".format(surpos)]["text"] = str(int(entry)+1)
        
    @staticmethod
    def find_surroundings(pos, rows, cols):
        upperbound = [i for i in range(cols)][1:]
        rightbound = [cols*(i+1)-1 for i in range(rows)][1:]
        lowerbound = [i for i in range((rows-1)*cols, rows*cols)][:-1]
        leftbound = [i*cols for i in range(rows)][:-1]

        if pos in upperbound:
            if pos == upperbound[-1]:
                sur = [pos-1,pos+cols-1,pos+cols]
            else:
                sur = [pos+1,pos+cols+1,pos+cols,pos+cols-1,pos-1]
        elif pos in rightbound:
            if pos == rightbound[-1]:
                sur = [pos-cols-1,pos-cols,pos-1]
            else:
                sur = [pos-cols-1,pos-cols,pos+cols,pos+cols-1,pos-1]
        elif pos in lowerbound:
            if pos == lowerbound[0]:
                sur = [pos-cols,pos-cols+1,pos+1]
            else:
                sur = [pos-cols-1,pos-cols,pos-cols+1,pos+1,pos-1]
        elif pos in leftbound:
            if pos == leftbound[0]:
                sur = [pos+1,pos+cols+1,pos+cols]
            else:
                sur = [pos-cols,pos-cols+1,pos+1,pos+cols+1,pos+cols]
        else:
            sur = [pos-cols-1,pos-cols,pos-cols+1,pos+1,pos+cols+1,pos+cols,pos+cols-1,pos-1]
    
        return sur
        
    @staticmethod
    def set_Field():
        for key in allFields.keys():
            allFields[key].configure(bg = "black")
    
    @staticmethod
    def revealer(lbl,rows,cols,oldlbls=[]):
        if lbl["bg"] != "black":
            pass
        elif lbl["text"] == "0":
            lbl.configure(bg="white",fg="white")
            for key,label in allFields.items():
                if label == lbl:
                    lblpos = int(key)
            sur = Minesweeper.find_surroundings(lblpos,rows,cols)
            for nextpos in sur:
                nextlbl = allFields[str(nextpos)]
                if nextlbl not in oldlbls:
                    oldlbls.append(nextlbl)
                    Minesweeper.revealer(nextlbl,rows,cols,oldlbls)
            Minesweeper.update_time(time.clock())
        elif lbl["text"] == "B":
            Minesweeper.revealLost()
        else:
            lbl["bg"] = "white"
            if lbl["text"] == "1":
                lbl["fg"] = "blue"
            elif lbl["text"] == "2":
                lbl["fg"] = "green"
            elif lbl["text"] == "3":
                lbl["fg"] = "red"
            elif lbl["text"] == "4":
                lbl["fg"] = "darkblue"
            elif lbl["text"] == "5":
                lbl["fg"] = "darkred"
            Minesweeper.update_time(time.clock())
        
        Minesweeper.check_for_win()
        
        
    @staticmethod
    def marker(lbl,count_Lbl,tot):
        nr = int(re.search("^[\d]+",count_Lbl["text"]).group())           
        if lbl["bg"] == "black":
            lbl.configure(fg = "darkred", bg = "darkred")
            nr += 1
            Minesweeper.update_time(time.clock())
        elif lbl["bg"] == "darkred":
            lbl.configure(fg = "black", bg = "black")
            nr -= 1
            Minesweeper.update_time(time.clock())
        
        count_Lbl["text"] = str(nr) + "/{}".format(tot)
        
    @staticmethod
    def questioner(lbl,count_Lbl,tot):
        nr = int(re.search("^[\d]+",count_Lbl["text"]).group())
        if lbl["bg"] == "darkred":
            lbl.configure(fg = "yellow", bg = "yellow")
            Minesweeper.update_time(time.clock())
            nr -= 1
        elif lbl["bg"] == "yellow":
            lbl.configure(fg = "black", bg = "black")
            Minesweeper.update_time(time.clock())
     
        count_Lbl["text"] = str(nr) + "/{}".format(tot)
        
    @staticmethod
    def revealLost():
        for lbl in allFields.values():
            lbl.configure(bg = "red", fg = "black")
        Minesweeper.update_time(time.clock())
        
    @staticmethod
    def revealWin():
        for lbl in allFields.values():
            lbl.configure(bg = "lightgreen", fg = "black")
        Minesweeper.update_time(time.clock())
        
    @staticmethod
    def check_for_win():
        nobomb = []
        for key,lbl in allFields.items():
            if int(key) not in bombpositions:
                nobomb.append(lbl)
        for nbomb in nobomb:
            if nbomb["bg"] != "white":
                return False
        else:
            Minesweeper.revealWin()
            
    @staticmethod
    def update_time(update):
        new = str(update - start_time)[0:5]
        time_L["text"] = "Time: " + new
    
    @staticmethod
    def helper(*args):
        root1 = Tk()
        root1.geometry('0x0-1+1')
        text = "Left click: Reveal a field. \n" \
              + "Right click: Mark as bomb (counted & blocked). \n" \
              + "Double right click: Mark as unsure (uncounted & blocked).\n\n" \
              + "Easy: 8x8 Field with 10 bombs. \n" \
              + "Medium: 16x16 Field with 40 bombs. \n" \
              + "Hard: 16x30 Field with 99 bombs."
              
        messagebox.showinfo(message=text)
        root1.destroy()
        
Minesweeper()