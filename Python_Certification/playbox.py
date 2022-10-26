from tkinter import *

def submit():
    username = entry.get()
    print(username)

window = Tk()
entry = Entry(window, font = ('Arial',50))
entry.pack(side = LEFT)
submit= Button(window,text = 'submit', command = submit)
submit.pack(side = RIGHT)
window.mainloop()