from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)

    new_pass = "".join(password_list)
    password.delete(0, END)
    password.insert(0, new_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #


dane = open("email_password", "a")
dane.close()
dane = open("email_password", "r")

dane_f = dane.readlines()
if len(dane_f) > 0:
    my_email = dane_f[-1]
    my_email = my_email.split("|")
    if len(my_email) > 1:
        my_email = my_email[1].strip()
    else:
        my_email = ""
else:
    my_email = ""
dane.close()
dane = open("email_password", "a")


def add_password():
    print("hi")
    if link.get().strip() != "" and e_user.get().strip() != "" and password.get().strip() != "":
        info = f'These are the details entered\nEmail : {e_user.get().strip()}\nPassword : {password.get().strip()}\nIs it ok to save?'
        is_ok = messagebox.askokcancel(link.get().strip(), info)
        if is_ok:
            dane.write(f"{link.get().strip()} | {e_user.get().strip()} | {password.get().strip()}\n")
            link.delete(0, END)
            password.delete(0, END)
    else:
        messagebox.showinfo("Ops", "Fields can't be empty")


# ---------------------------- GUI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)
web = Label(text="Website")
web.grid(row=1, column=0)
email = Label(text="Email/Username")
email.grid(row=2, column=0)
p_word = Label(text="Password")
p_word.grid(row=3, column=0)
link = Entry(width=39)
link.grid(row=1, column=1, columnspan=2)
e_user = Entry(width=39)
e_user.grid(row=2, columnspan=2, column=1)
password = Entry(width=21)
password.grid(row=3, column=1)
adding = Button(text="Add", width=36, command=add_password)
adding.grid(row=4, column=1, columnspan=2)
g_pass = Button(text="Generate Password", command=generate_pass)
g_pass.grid(row=3, column=2)
link.focus()
e_user.insert(0, my_email)

window.mainloop()
dane.close()
