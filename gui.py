from tkinter import *

# class Application:
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()

#         self.print_button = Button(frame, text="Print Message", command=self.print_message)
#         self.print_button.pack(side=LEFT)
        
#         self.quit_button = Button(frame, text="Quit", command=frame.quit)
#         self.quit_button.pack(side=LEFT)

#     def print_message(self):
#         print("Hey this is working!")

root = Tk()
menu = Menu(root)
root.config(menu=menu)

def do_nothing():
    print("I am doing nothing")

sub_menu = Menu(menu)
sub_menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="New...", command=do_nothing)
# sub_menu.add_command(label="New project", command=do_nothing)
# sub_menu.add_separator()
# sub_menu.add_command(text="Quit", command=root.quit)

# edit_menu = Menu(menu)
# menu.add_cascade(label="Edit", menu=edit_menu)
# edit_menu.add_command(label="Redo", command=do_nothing)


# app = Application(root)
root.mainloop()