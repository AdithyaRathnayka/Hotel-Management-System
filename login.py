from tkinter import *
import tkinter.messagebox as MessageBox

window_login = Tk()
window_login.title("Royal reception hall")
window_login.geometry('500x300')
window_login.configure(bg="light blue")

def login():
    username = textbox1.get()
    password = (textbox2.get())
    if username == "royalhotel" and password == "202128":
        MessageBox.showinfo(username, "login success")
        window_login.destroy()
        import page1
    else:
        MessageBox.showinfo(username, "wrong username or password ")


label1 = Label(window_login, text="Username", font=18)
label1.grid(row=10, column=8)
label2 = Label(window_login, text="Password", font=18)
label2.grid(row=12, column=8)

textbox1 = Entry(window_login, fg='blue')
textbox1.grid(row=10, column=9,)
textbox2 = Entry(window_login, show="*")
textbox2.grid(row=12, column=9, )

logbutton = Button(window_login, height="1", command=login, width="10",  text="login")
logbutton.grid(row=15, column=9)

window_login.mainloop()


