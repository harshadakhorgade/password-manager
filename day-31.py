from tkinter import *
from tkinter import messagebox

window =Tk()
window.title("Password Manager")
window.config(padx= 200,pady=200)


yes_button = Button(text ="yes" )
yes_button.grid(column=1, row=2 )

no_button = Button(text ="no" )
no_button.grid(column=2, row=2 )


window.mainloop()