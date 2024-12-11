from tkinter import *
from tkinter import messagebox
from random import shuffle,randint,choice
import pyperclip

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_genrate():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# list comprehension

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list= password_letters + password_symbols + password_numbers


    shuffle(password_list)

    password ="".join(password_list)

    pass_input.insert(0,password)
    # it will automatically copy password after clicking on generate button
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():

    w_input = (website_input.get())
    u_input =(username_input.get())
    p_input =(pass_input.get())

    if len(w_input)==0 or len(p_input) == 0:
        messagebox.showinfo(title="Ooops", message=f"make sure you haven't left any fields blank!!!")

    else:
        is_ok= messagebox.askokcancel(title= "website",message=f"These are the details entered :\nwebsite :{w_input}\n"
                                                        f"Email :{u_input}\nPassword{p_input}")

        if is_ok:
            with open("mydata.txt", "a") as file:
                file.write(f"{w_input}   |   {u_input}    |   {p_input} \n")
                # clear the entry
                website_input.delete(0,END)
                pass_input.delete(0, END)






# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Pomodoro")
window.config(padx= 50,pady=50)

canvas =Canvas(width=200,height=200,highlightthickness=0)
logo_img= PhotoImage(file="logo.png")
canvas.create_image(100,100,image =logo_img)
canvas.grid(column =1,row=0)

website_label1= Label(text="Website:",font=(FONT_NAME,10))
website_label1.grid(column=0, row=1)

user_label2= Label(text="Email/Username:",font=(FONT_NAME,10))
user_label2.grid(column=0, row=2)

pass_label2= Label(text="Password:",font=(FONT_NAME,10))
pass_label2.grid(column=0, row=3)


website_input = Entry(width=35)
website_input.grid(column=1, row=1,columnspan =3)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(column=1, row=2,columnspan =3)
username_input.insert(0,"harshada123@gmail.com")

pass_input = Entry(width=17)
pass_input.grid(column=1, row=3)

Genrate_button = Button(text ="Generate Password",command=pass_genrate)
Genrate_button .grid(column=2, row=3)

add_button = Button(text ="Add" ,width=30,command=add_info)
add_button.grid(column=1, row=4 ,columnspan=2)


window.mainloop()