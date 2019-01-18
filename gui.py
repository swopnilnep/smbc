from tkinter import *

# Base window of the program
base = Tk()

label_name = Label(base, text="Name")
label_password = Label(base, text="Password")
entry_name = Entry(base)
entry_password = Entry(base)

label_name.grid(row=0, sticky=E)
entry_name.grid(row=0, column=1)
label_password.grid(row=1, sticky=E)
entry_password.grid(row=1, column=1)

def print_name():
    print("Hello World!")

c = Checkbutton(base, text="Keep me logged in")
c.grid(columnspan=2)

button1 = Button(base, command=print_name)

# Loop until cross is pressed
base.mainloop()