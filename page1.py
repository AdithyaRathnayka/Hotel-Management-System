from tkinter import *

window_h_con = Tk()
window_h_con.title("Royal reception hall")
window_h_con.geometry('850x400')
window_h_con.configure(bg="light blue")

def goldenhall():
    window_h_con.destroy()
    import page2

def silverhall():
    window_h_con.destroy()
    import page3

def bronzehall():
    window_h_con.destroy()
    import page4


labelmenu = Label(window_h_con, text="Hall Conditions", font="times 30 bold", bg="gray")
labelmenu.grid(row=1, column=7)
l_hall1 = Label(window_h_con, text=" Golden hall", font=20)
l_hall1.grid(row=4, column=0)
l_hall2 = Label(window_h_con, text="Silver hall", font=20)
l_hall2.grid(row=7, column=0)
l_hall3 = Label(window_h_con, text="  Bronze hall", font=20)
l_hall3.grid(row=10, column=0)
l_halLA_1 = Label(window_h_con, text="A/C", font=20)
l_halLA_1.grid(row=4, column=7)
l_halLA_2 = Label(window_h_con, text="A/C", font=20)
l_halLA_2.grid(row=7, column=7)
l_hallA_3 = Label(window_h_con, text="Non A/C", font=20)
l_hallA_3.grid(row=10, column=7)
l_hallP_1 = Label(window_h_con, text="Maximum 1500 seats", font=20)
l_hallP_1.grid(row=4, column=9)
l_hallP_2 = Label(window_h_con, text="Maximum 1000 seats", font=20)
l_hallP_2.grid(row=7, column=9)
l_hallP_3 = Label(window_h_con, text="Maximum 500 seats", font=20)
l_hallP_3.grid(row=10, column=9)

lbl = Label(window_h_con, text="Select the hall", font="bold, 20", fg="purple")
lbl.grid(row=50, column=0)
G_btn = Button(window_h_con, text="Golden Hall", command=goldenhall, font=12, bg="gray", fg="white")
G_btn.grid(row=55, column=3)
S_btn = Button(window_h_con, text="Silver Hall", command=silverhall, font=12,bg="gray", fg="white")
S_btn.grid(row=56, column=3)
B_btn = Button(window_h_con, text="Bronze Hall", command=bronzehall, font=12,bg="gray", fg="white")
B_btn.grid(row=57, column=3)


window_h_con.mainloop()
