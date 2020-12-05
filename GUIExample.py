# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 17:35:46 2016

@author: Spider Schwein
"""

from tkinter import *
from tkinter import ttk

"""""""""
TABLE OF CONTENTS:
    1) Example: Feet to meters (32)
    2) Example: Binding to root, Clicks, drags (73)
    3) Linking a (String)Var (87)
    http://www.tkdocs.com/tutorial/widgets.html
    4) Button,Checkbutton,Radiobutton,Entry,Combobox (101)
    5) Example: Framelayout (168)
    http://www.tkdocs.com/tutorial/morewidgets.html
    6) Good Example: Listbox, full interface (223)
    7) #Example Listbox, Scrollbar, Sizegrip (334)
    http://www.tkdocs.com/tutorial/menus.html 
    8) Menus (351)
    9) Windows (392)
    10) Standard Dialogs,colorchooser,messagebox (418)
    http://www.tkdocs.com/tutorial/canvas.html
    11) Canvas (441)
    12) Text(514)
    13)
 
"""""""""
#Example: Feet to meters
"""
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
"""




#Example: Binding to root, Clicks, drags
"""
root = Tk()
l =ttk.Label(root, text="Starting...")
l.grid()
root.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
root.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
root.bind('<1>', lambda e: l.configure(text='Clicked left mouse button'))
root.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
root.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
root.mainloop()
"""


#Linking a (String)Var
"""
root = Tk()
frame = ttk.Frame(master=root, padding = "3 3 10 10")
frame["borderwidth"] = 2
frame["relief"] = "solid"
label = ttk.Label(root,text ='Full name')
resultsContents = StringVar()
label["textvariable"] = resultsContents
resultsContents.set("NEW")
label.grid()
"""


#Button 
"""
root = Tk()
button = ttk.Button(root, text='Okay', default = "active") #active: gets triggered by Enter
button.grid()
button.state(['!disabled'])            # set the disabled flag, disabling the button
button.state(['disabled'])           # clear the disabled flag
print(button.instate(['disabled']))         # return true if the button is disabled, else false
print(button.instate(['!disabled']))     # return true if the button is not disabled, else false
#button.instate(['!disabled'], cmd)    # execute 'cmd' if the button is not disabled
#The full list of state flags available to themed widgets is: "active", "disabled", "focus", "pressed", "selected", "background", "readonly", "alternate", and "invalid".



#Checkbutton

measureSystem = StringVar()
check = ttk.Checkbutton(root, text='Use Metric', 
	    command=None, variable=measureSystem,
	    onvalue='metric', offvalue='imperial')
check.state(['!disabled'])            
check.state(['disabled'])       
print(check.instate(['disabled']))        
print(check.instate(['!disabled'])) 
check.grid()



#Radiobutton

phone = StringVar()
test =StringVar()
home = ttk.Radiobutton(root, text='Home', variable=phone, value='home')
office = ttk.Radiobutton(root, text='Office', variable=phone, value='office')
cell = ttk.Radiobutton(root, text='Mobile', variable=phone, value='cell')
test = ttk.Radiobutton(root, text= "Test", variable = test, value= "Test")
home.grid()
office.grid()
cell.grid()
test.grid()



#Entry

username = StringVar()
name = ttk.Entry(root, textvariable=username)
name.delete(0,'end')          # delete between two indices, 0-based
name.insert(0, 'our name')   # insert new text at a given index
print('current value is %s' % name.get())
name.grid()
password = ttk.Entry(root, textvariable="username",show="*")
password.grid()



#Combobox

countryvar = StringVar()
country = ttk.Combobox(root, textvariable=countryvar, )
country['values'] = ('USA', 'Canada', 'Australia')
country.state(["readonly"]) #one cannot write own things in the box
country.grid()
root.mainloop()
"""


#Example: Framelayout
"""
root = Tk()

content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(True)
twovar.set(False)
threevar.set(True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)
content.grid_slaves()
for w in content.grid_slaves(): print(w)
print("\n")
for w in content.grid_slaves(row=3): print(w)
print("\n")
for w in content.grid_slaves(column=0): print(w)
namelbl.grid_info()
namelbl.grid_configure(sticky=(E,W))
namelbl.grid_info()

root.mainloop()
"""


#Good Example: Listbox, full interface
"""
root = Tk()

# Initialize our country "databases":
#  - the list of country codes (a subset anyway)
#  - a parallel list of country names, in the same order as the country codes
#  - a hash table mapping country code to population<
countrycodes = ('ar', 'au', 'be', 'br', 'ca', 'cn', 'dk', 'fi', 'fr', 'gr', 'in', 'it', 'jp', 'mx', 'nl', 'no', 'es', 'se', 'ch')
countrynames = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
        'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
        'Sweden', 'Switzerland')
cnames = StringVar(value=countrynames)
populations = {'ar':41000000, 'au':21179211, 'be':10584534, 'br':185971537, \
        'ca':33148682, 'cn':1323128240, 'dk':5457415, 'fi':5302000, 'fr':64102140, 'gr':11147000, \
        'in':1131043000, 'it':59206382, 'jp':127718000, 'mx':106535000, 'nl':16402414, \
        'no':4738085, 'es':45116894, 'se':9174082, 'ch':7508700}

# Names of the gifts we can send
gifts = { 'card':'Greeting card', 'flowers':'Flowers', 'nastygram':'Nastygram'}

# State variables
gift = StringVar()
sentmsg = StringVar()
statusmsg = StringVar()

# Called when the selection in the listbox changes; figure out
# which country is currently selected, and then lookup its country
# code, and from that, its population.  Update the status message
# with the new population.  As well, clear the message about the
# gift being sent, so it doesn't stick around after we start doing
# other things.
def showPopulation(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        code = countrycodes[idx]
        name = countrynames[idx]
        popn = populations[code]
        statusmsg.set("The population of %s (%s) is %d" % (name, code, popn))
    sentmsg.set('')

# Called when the user double clicks an item in the listbox, presses
# the "Send Gift" button, or presses the Return key.  In case the selected
# item is scrolled out of view, make sure it is visible.
#
# Figure out which country is selected, which gift is selected with the 
# radiobuttons, "send the gift", and provide feedback that it was sent.
def sendGift(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = countrynames[idx]
        # Gift sending left as an exercise to the reader
        sentmsg.set("Sent %s to leader of %s" % (gifts[gift.get()], name))

# Create and grid the outer content frame
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

# Create the different widgets; note the variables that many
# of them are bound to, as well as the button callback.
# Note we're using the StringVar() 'cnames', constructed from 'countrynames'
lbox = Listbox(c, listvariable=cnames, height=5)
lbl = ttk.Label(c, text="Send to country's leader:")
g1 = ttk.Radiobutton(c, text=gifts['card'], variable=gift, value='card')
g2 = ttk.Radiobutton(c, text=gifts['flowers'], variable=gift, value='flowers')
g3 = ttk.Radiobutton(c, text=gifts['nastygram'], variable=gift, value='nastygram')
send = ttk.Button(c, text='Send Gift', command=sendGift, default='active')
sentlbl = ttk.Label(c, textvariable=sentmsg, anchor='center')
status = ttk.Label(c, textvariable=statusmsg, anchor=W)

# Grid all the widgets
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
lbl.grid(column=1, row=0, padx=10, pady=5)
g1.grid(column=1, row=1, sticky=W, padx=20)
g2.grid(column=1, row=2, sticky=W, padx=20)
g3.grid(column=1, row=3, sticky=W, padx=20)
send.grid(column=2, row=4, sticky=E)
sentlbl.grid(column=1, row=5, columnspan=2, sticky=N, pady=5, padx=5)
status.grid(column=0, row=6, columnspan=2, sticky=(W,E))
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)

# Set event bindings for when the selection in the listbox changes,
# when the user double clicks the list, and when they hit the Return key
lbox.bind('<<ListboxSelect>>', showPopulation)
lbox.bind('<Double-1>', sendGift)
root.bind('<Return>', sendGift)
            
# Colorize alternating lines of the listbox
for i in range(0,len(countrynames),2):
    lbox.itemconfigure(i, background='#f0f0ff')

# Set the starting state of the interface, including selecting the
# default gift to send, and clearing the messages.  Select the first
# country in the list; because the <<ListboxSelect>> event is only
# generated when the user makes a change, we explicitly call showPopulation.
gift.set('card')
sentmsg.set('')
statusmsg.set('')
lbox.selection_set(0) #also possible to give startindex, endindex to select more than one
showPopulation()

root.mainloop()
"""


#Example Listbox, Scrollbar, Sizegrip
"""
root = Tk()
l = Listbox(root, height=5)
l.grid(column=0, row=0, sticky=(N,W,E,S))
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N,S))
l['yscrollcommand'] = s.set
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
for i in range(1,101):
    l.insert('end', 'Line %d of 100' % i)
root.mainloop()
"""


#Menus

"""
root = Tk()
root.option_add('*tearOff', FALSE)

win = Toplevel(root)
menubar = Menu(win)
win['menu'] = menubar

menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')

menu_file.add_command(label='New', command= None) #None=newFile
menu_file.add_command(label='Open...', command=None) #None=openFile
menu_file.add_command(label='Close', command=None) #None=closeFile

menu_file.add_separator()

check = StringVar()
menu_file.add_checkbutton(label='Check', variable=check, onvalue=1, offvalue=0)
radio = StringVar()
menu_file.add_radiobutton(label='One', variable=radio, value=1)
menu_file.add_radiobutton(label='Two', variable=radio, value=2)

root.mainloop()

root = Tk()
menu = Menu(root)
for i in ('One', 'Two', 'Three'):
    menu.add_command(label=i)
if (root.tk.call('tk', 'windowingsystem')=='aqua'):
    root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
    root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
else:
    root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))
"""


#Windows
"""
root = Tk()
t = Toplevel()
t.title("Toplevel")
#t.destroy()
t.geometry('300x200-5+40')
#window.lift()           #controls which window overlaps the other
#window.lift(otherwin)
#window.lower()
#window.lower(otherwin)
t.resizable(FALSE,FALSE)

root.minsize(200,100)
root.maxsize(500,500)

little = ttk.Label(root, text="Little")
bigger = ttk.Label(root, text='Much bigger label')
little.grid(column=0,row=0)
bigger.grid(column=0,row=0)
root.after(2000, lambda: little.lift())
root.mainloop()
"""



#Standard Dialogs,colorchooser, messagebox

"""
root = Tk()
b = Button(root)
b.grid()
#from tkinter import filedialog
#filename = filedialog.askopenfilename()
#filename = filedialog.asksaveasfilename()
#dirname = filedialog.askdirectory()
#
#from tkinter import colorchooser
#colorchooser.askcolor(initialcolor='#ff0000')
#
from tkinter import messagebox
#messagebox.showinfo(message='Have a good day')
messagebox.askyesno( \
	   message='Are you sure you want to install SuperVirus?', \
	   icon='question', title='Install')
#askokcancel, askquestion, askretrycancel, askyesno, askyesnocancel, showerror, showinfo, showwarning.
root.destroy()
root.mainloop()
"""



#Canvas
"""
root = Tk()

h = ttk.Scrollbar(root, orient=HORIZONTAL)
v = ttk.Scrollbar(root, orient=VERTICAL)
canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview
ttk.Sizegrip(root).grid(column=1, row=1, sticky=(S,E))

canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', 'paletteSelected')
    canvas.itemconfigure('palette', outline='white')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
    canvas.itemconfigure('paletteSelected', outline='#999999')

def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
    lastx, lasty = x, y

def doneStroke(event):
    canvas.itemconfigure('currentline', width=1)        
        
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", doneStroke)

id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

setColor('black')
canvas.itemconfigure('palette', width=5)



c = Canvas(root)
print(c.create_line(10, 10, 20, 20, tags=('firstline', 'drawing')))

print(c.create_rectangle(30, 30, 40, 40, tags=('drawing')))

c.addtag('rectangle', 'withtag', 2)
c.addtag('polygon', 'withtag', 'rectangle')
print(c.gettags(2))
c.dtag(2, 'polygon')
print(c.gettags(2))
print(c.find_withtag('drawing'))

root.mainloop()
"""



#Text
"""
root = Tk()
text = Text(root, width=40, height=10)
text.grid()
text.insert('1.0', 'here is my text to insert')
thetext = text.get('1.0', 'end')
print(thetext)

#3.end	The newline at the end of line 3.
#1.0 + 3 chars	Three characters past the start of line 1.
#2.end -1 chars	The last character before the new line in line 2.
#end -1 chars	The newline that Tk always adds at the end of the text.
#end -2 chars	The actual last character of the text.
#end -1 lines	The start of the last actual line of text.
#2.2 + 2 lines	The third character (index 2) of the fourth line of text.
#2.5 linestart	The first character of line 2.
#2.5 lineend	The position of the newline at the end of line 2.
#2.5 wordstart	The first character of the word containing the character at index 2.5.
#2.5 wordend	The first character just past the last character of the word containing index 2.5.

text.delete('1.0', '2.0')

root = Tk()
log = Text(root, state='disabled', width=80, height=24, wrap='none')
log.grid()

def writeToLog(msg):
    numlines = log.index('end - 1 line').split('.')[0]
    log['state'] = 'normal'
    if numlines==24:
        log.delete(1.0, 2.0)
    if log.index('end-1c')!='1.0':
        log.insert('end', '\n')
    log.insert('end', msg)
    log['state'] = 'disabled'
    
root.mainloop()
"""