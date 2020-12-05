from tkinter import *
from tkinter import ttk

class SET(object):    
    pos = None
    def __init__(self,name,length,totposi,invalid):
        revletters = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J"}
        totposi=[(revletters[pos[0]], pos[1]) for pos in totposi] 
        invalid=[(revletters[pos[0]], pos[1]) for pos in invalid]
        global root, msg2, msg3
        root = Tk()
        root.title("{} setting".format(name))
        root.minsize(400,250)
        root.geometry('650x550+30+30')
        for i in range(12):
            root.grid_columnconfigure(i, weight = 1)
        for i in range(12):
            root.grid_rowconfigure(i, weight = 1)
        ttk.Sizegrip().grid(row=11,column=11, sticky=(S,E))
        
        letters = ["A","B","C","D","E","F","G","H","I","J"]
        numbers = [str(i) for i in range(1,11)]  
              
        msg1 = ttk.Label(root, text = "Selected Position: None")
        msg1.grid(row=11,column=0)
        msg2 = ttk.Label(root, text = "Start: None")
        msg2.grid(row=3,column=0)
        msg3 = ttk.Label(root, text = "End/Orientation: None")
        msg3.grid(row=4,column=0)
        setbutton = ttk.Button(root, text= "Set",default='active',command=SET.SET)
        setbutton.grid(row=5,column=0)
        exitButton = ttk.Button(root, text = "Exit Game", command=SET.leave)
        exitButton.grid(row=0, column=0)  
        turn = ttk.Label(root, text = "Choose a position for your {} (length {})!".format(name,length))
        turn.grid(row=2,column=0)
        helpbutton = ttk.Button(root, text = "Help",command=SET.helper)
        helpbutton.grid(row=9, column=0)
        selectButton = ttk.Button(root, text = "Select Music", command=SET.select)
        selectButton.grid(row=8,column=0)
        
        
        allLabels = {}
        
        count = 0
        enter_field = lambda x: (lambda p: msg1.configure(text="Selected Position: {}{}".format(x[0],x[1])))
        select_start = lambda x: (lambda p: msg2.configure(text="Start: {}{}".format(x[0],x[1])))
        select_end = lambda x: (lambda p: msg3.configure(text="End/Orientation: {}{}".format(x[0],x[1])))
        for letter in letters:
            for number in numbers:
                lbl = Label(root, text = '{}{}'.format(letter,number), bg="lightblue")
                allLabels['{}{}'.format(letter,number)] = lbl
                lbl.grid(row=count+1, column=int(number)+1)
                lbl.bind('<Enter>', enter_field((letter,number)))
                lbl.bind('<1>', select_start((letter,number)))
                lbl.bind('<3>', select_end((letter,number)))
                lbl.bind('<Double-1>', select_end((letter,number)))
            count += 1         
        
        for pos in totposi:
            allLabels["{}{}".format(pos[0],pos[1])]["bg"] = "green"
        
        for pos in invalid:
            allLabels["{}{}".format(pos[0],pos[1])]["bg"] = "red"
            
        root.bind('<Return>', SET.SET)  
        
        root.mainloop()
    
    def SET(*args):      
        SET.pos= msg2['text'][7:] + " " + msg3['text'][17:]
        root.destroy() 
  
    def leave(*args):
        SET.pos = "exit"
        root.destroy()
        
    def helper(*args):
        SET.pos = "help"
        root.destroy()
        
    def select(*args):
        SET.pos = "select sound"
        root.destroy()
        
#SET("name",3,[],[])