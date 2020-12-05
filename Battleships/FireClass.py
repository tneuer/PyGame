# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 20:03:01 2016

@author: Spider Schwein
"""

from tkinter import *
from tkinter import ttk

class Fire(object):    
    pos = None
    def __init__(self,name,positions):
        global msg1
        revletters = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J"}
        missed = []
        hitted = []
        for i in range(1,11):
            for j in range(1,11):
                if positions[i-1][j-1] == "~":
                    missed.append((revletters[i],j))                 
                elif positions[i-1][j-1] == "X":
                    hitted.append((revletters[i],j))
                    
        global root, msg2
        root = Tk()
        root.title("Target Selection")
        root.minsize(400,250)
        root.geometry('650x550+30+30')
        for i in range(12):
            root.grid_columnconfigure(i, weight = 1)
        for i in range(12):
            root.grid_rowconfigure(i, weight = 1)
        ttk.Sizegrip().grid(row=11,column=11, sticky=(S,E))
        
        letters = ["A","B","C","D","E","F","G","H","I","J"]
        numbers = [str(i) for i in range(1,11)]  
              
        msg1 = ttk.Label(root, text = "Selected Target: None")
        msg1.grid(row=11,column=0)
        msg2 = ttk.Label(root, text = "Fixed Target: None")
        msg2.grid(row=3,column=0)
        firebutton = ttk.Button(root, text= "Fire!",default='active',command=Fire.fire)
        firebutton.grid(row=4,column=0)
        exitButton = ttk.Button(root, text = "Exit Game", command=Fire.leave)
        exitButton.grid(row=0, column=0)  
        turn = ttk.Label(root, text = "{}, choose a postion to shoot at!".format(name))
        turn.grid(row=2,column=0)
        helpbutton = ttk.Button(root, text = "Help",command=Fire.helper)
        helpbutton.grid(row=9, column=0)
        selectButton = ttk.Button(root, text = "Select Music", command=Fire.select)
        selectButton.grid(row=8,column=0)
        reportButton = ttk.Button(root, text = "Damage Report", command = Fire.damage)
        reportButton.grid(row=6,column=0)
        changeButton = ttk.Button(root, text = "Change Name", command = Fire.change)
        changeButton.grid(row=7,column=0)
        
        
        allLabels = {}
        
        count = 0
        enter_field = lambda x: (lambda p: Fire.enter((x[0],x[1],x[2])))
        select_start = lambda x: (lambda p: msg2.configure(text="Fixed Target: {}{}".format(x[0],x[1])))
        leave_field = lambda x: (lambda p: x.configure(bg=oldcolor))
        for letter in letters:
            for number in numbers:
                lbl = Label(root, text = '{}{}'.format(letter,number), bg="lightblue")
                allLabels['{}{}'.format(letter,number)] = lbl
                lbl.grid(row=count+1, column=int(number)+1)
                lbl.bind('<Enter>', enter_field((letter,number,lbl)))
                lbl.bind('<Leave>', leave_field(lbl))
                lbl.bind('<1>', select_start((letter,number)))
                lbl.bind('<Double-1>', Fire.fire)
            count += 1         
        
            
        for pos in missed:
            allLabels["{}{}".format(pos[0],pos[1])]["bg"] = "blue"
        
        for pos in hitted:
            allLabels["{}{}".format(pos[0],pos[1])]["bg"] = "red"
        
        root.bind('<Return>', Fire.fire)    
        root.mainloop()
    
    def fire(*args):      
        Fire.pos=msg2['text'][14:]
        root.destroy() 
  
    def leave(*args):
        Fire.pos = "exit"
        root.destroy()
        
    def helper(*args):
        Fire.pos = "help"
        root.destroy()
        
    def select(*args):
        Fire.pos = "select sound"
        root.destroy()
        
    def damage(*args):
        Fire.pos = "damage report"
        root.destroy()
        
    def change(*args):
        Fire.pos = "change name"
        root.destroy()
        
    def enter(x):
        global oldcolor
        oldcolor = x[2]["bg"]
        msg1.configure(text="Selected Target: {}{}".format(x[0],x[1]))
        x[2].configure(bg="orange")
    
#Fire("Herbert", [[" " for i in range(10)] for i in range(10)])