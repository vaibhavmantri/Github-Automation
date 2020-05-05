from tkinter import *
from first_automation import github
root = Tk()
canvas1 = Canvas(root, width = 500, height = 300)
canvas1.pack()
root.title("Login github")
# Github Username
entry1 = Label(root,text = "Email/Username")
e1 = Entry(root, bd=5)
e1.pack(side = LEFT)
# Github Password
entry2 = Label(root, text = "Password")
e2 = Entry(root,bd = 5)
e2.pack(side = RIGHT)

def callfun():
    github(e1,get(),e2.get())
btn = Button(root,text = "click", command = callfun)
btn.pack()
root.mainloop()