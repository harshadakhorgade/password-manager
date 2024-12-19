from tkinter import *
from tkinter import messagebox
from random import shuffle,randint,choice
import pyperclip
import json

FONT_NAME = "Courier"

# ---------------------------- Search Data ------------------------------- #
def search_info():
    w_input = (website_input.get())
    u_input = (username_input.get())
    p_input = (pass_input.get())
    try:
        with open("mydata.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data file found")
    else:
        if w_input in data:
            email =data[w_input]["email"]
            password =data[w_input]["password"]
            messagebox.showinfo(title = w_input, message=f"Email :{email} \nPassword :{password}")
        else:
            messagebox.showinfo(title="Error", message=f"The {w_input} is not  Exist in data")




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
    new_data= {
        w_input :{
            "email":u_input ,
            "password":p_input

         }
    }

    if len(w_input)==0 or len(p_input) == 0:
        messagebox.showinfo(title="Ooops", message=f"make sure you haven't left any fields blank!!!")

    else:
        try:
             with open("mydata.json", "r") as file:
                    # reading old data
                    data = json.load(file)
                    print(type(data))
                 
        except FileNotFoundError:

            with open("mydata.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
                # updating old data with new data
                data.update(new_data)

                with open("mydata.json", "w") as file:
                    json.dump(data, file, indent=4)

        finally:
                # clear the entry
                website_input.delete(0,END)
                pass_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Password Manager")
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


website_input = Entry(width=17)
website_input.grid(column=1, row=1)
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

search_button = Button(text ="Search" ,command=search_info,width=10)
search_button.grid(column=2, row=1 )


window.mainloop()