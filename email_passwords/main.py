from tkinter import *
from tkinter import messagebox
import json
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


dane_f = open("email_password.json", "a")
dane_f.close()
dane_f = open("email_password.json", "r")
try:
    dane = json.load(dane_f)
except json.decoder.JSONDecodeError:
    dane = {}
    my_email = ""
else:
    all_emails = [rest["Email"] for key, rest in dane.items()]
    my_email = all_emails[-1]
dane_f.close()


def add_password():
    if link.get().strip() != "" and e_user.get().strip() != "" and password.get().strip() != "":
        info = f'These are the details entered\nEmail : {e_user.get()}\nPassword : {password.get()}\nIs it ok to save?'
        is_ok = messagebox.askokcancel(link.get(), info)
        if is_ok:
            with open("email_password.json", "w") as dane_j:
                dane.update({link.get(): {"Email": e_user.get(), "Password": password.get()}})
                json.dump(dane, dane_j, indent=4)
            link.delete(0, END)
            password.delete(0, END)
    else:
        messagebox.showinfo("Ops", "Fields can't be empty")


def search_data():
    if link.get() in dane:
        email_pass = dane[link.get()]
        message = f'Email : {email_pass["Email"]}\nPassword : {email_pass["Password"]}'
        messagebox.showinfo(title="Search", message=message)
    else:
        messagebox.showinfo(title="Search", message="No password found to this website")
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
link = Entry(width=25)
link.grid(row=1, column=1,)
e_user = Entry(width=50)
e_user.grid(row=2, columnspan=2, column=1)
password = Entry(width=25)
password.grid(row=3, column=1)
adding = Button(text="Add", width=36, command=add_password)
adding.grid(row=4, column=1, columnspan=2)
g_pass = Button(text="Generate Password", command=generate_pass, width=20)
g_pass.grid(row=3, column=2)
search = Button(text="Search", command=search_data, width=20)
search.grid(column=2, row=1)
link.focus()
e_user.insert(0, my_email)

window.mainloop()

