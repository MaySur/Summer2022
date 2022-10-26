from tkinter import *
def click():
    username = fnameEntry.get()
    print(username)
window = Tk()
window.geometry ('420x420')
window.title('Workout Project')
window.config(background = '#66d1c8')

fnameLabel = Label(window, text ='Name: ',font=('Arial',10,'bold'),relief = RAISED, bd = 5)
fnameLabel.place(x=1,y=0)
fnameEntry = Entry(window)
fnameEntry.grid(row=0, column =1)


lnameLabel = Label(window, text ='Last Name: ')
lnameLabel.grid(row =1, column=0)
lnameEntry = Entry(window)
lnameEntry.grid(row=1, column =1)

emailLabel = Label(window, text ='Email: ')
emailLabel.grid(row =2, column=0)
emailEntry = Entry(window)
emailEntry.grid(row=2, column =1)

submitButton = Button(window,text = 'Submit', command = click)
submitButton.grid(row=3, column =0, columnspan=2)


window.mainloop()