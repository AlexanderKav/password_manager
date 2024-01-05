from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ("".join(password_list))

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_input.get()) or len(password_input.get()) == 0:
        messagebox.showinfo(title="Oops", message=f"Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details you have entered: \nEmail: {username_input.get()} \nPassword: {password_input.get()} \nIs it ok to save?")
        if is_ok:
                file = open("data.txt", "a")
                file.write(f"{website_input.get()} | {username_input.get()} | {password_input.get()}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
                file.close()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_img)
canvas.grid(column=1, row=0)



website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)



website_input = Entry(width=52)
website = website_input.get()
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

username_input = Entry(width=52,)
email = username_input.get()
username_input.focus()
username_input.insert(0,"alexkavanagh6@gmail.com")
username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=33)
password = password_input.get()
password_input.focus()
password_input.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45,  command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
