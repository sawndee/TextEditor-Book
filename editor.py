from tkinter import *


def doNothing():
    print("Ok i will do something hah!")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New ...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Get it...", command=doNothing)

# ********* creating TOOLBAR *********


toolbar = Frame(root)
insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)


# ***********Status BAR***********


status = Label(root, text="Word Count", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


# *********** TEXT AREA FOR TYPING **************
S = Scrollbar(root)
T = Text(root, height=50, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill='both', expand=TRUE)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(END, quote)


root.mainloop()