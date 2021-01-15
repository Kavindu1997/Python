from tkinter import *
 
window = Tk()
window.title("TODO-list")
 
content = Listbox(window, font="Ariel 24 bold")
task = StringVar()
e = Entry(window, textvariable=task, font="Ariel 24")
add = Button(window, text="ADD", font="Ariel 20", padx=30,
command= lambda content=content, task=task : content.insert(END,task.get()))
delete = Button(window, text="DELETE",font="Ariel 20", 
command= lambda content=content : content.delete(ANCHOR))
 
content.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 10)
e.grid(row=1, column = 0, columnspan = 2, padx = 5, pady = 10)
add.grid(row = 2, column = 0, padx = 5, pady = 20)
delete.grid(row = 2, column = 1, padx = 5, pady = 20)
window.mainloop()

#------------------------------------------------------------------------------



from tkinter import *
from tkinter import filedialog
 
def saveFile():
    f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:
        return
    try:
        textUserWrote = str(content.get(1.0, END))
        f.write(textUserWrote)
    except:
        print("Cannot save the file")
    finally:
        f.close()
 
def openFile():
    try:
        t = filedialog.askopenfile(mode="r", title="Select File", 
        filetypes=[("All Files", "*.*")])
        content.insert(END, t.read())
    except:
        print("Cannot load the file")
    finally:
        if t:
            t.close()
 
def closeWindow():
    window.destroy()
 
window = Tk()
 
mainMenu = Menu(window)
window.config(menu=mainMenu)
 
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=closeWindow)
mainMenu.add_command(label="Help")
 
content = Text(window, width=100)
 
content.grid(row=0,column=0, padx=5,pady=5)
 
window.mainloop()


#------------------------------------------------------------------------------------


from tkinter import *
 
window = Tk()
 
def callback(event):
    c.create_oval(event.x - 5, event.y - 5, 
    event.x + 5, event.y + 5, fill="#558832")
def draw(event):
    c.create_oval(event.x - 5, event.y - 5, 
    event.x + 5, event.y + 5, fill="#000000")
def drawRectangle(event):
    global draw,x1,y1
    if draw:
        c.create_rectangle(x1, y1, event.x, event.y, fill="Red")
        draw = False
    else:
        x1 = event.x
        y1 = event.y
        draw = True
 
 
c = Canvas(window, width=400, height=400)
c.pack()
c.bind("<Button-1>", callback)
c.bind("<B1-Motion>", draw)
c.bind("<Button-3>", drawRectangle)
draw = False
x1 = 0
y1 = 0
window.mainloop()