from tkinter import *

window_silver_hall = Tk()
window_silver_hall.title("Silver hall menus")
window_silver_hall.geometry('625x650')

def exit():
    window_silver_hall.destroy()

def page5():
    window_silver_hall.destroy()
    import page5


menu1 = Label(window_silver_hall, text="Silver Hall Menus", font="20", fg="gold", bg="gray")
menu1.grid(row=0, column=5)

menuA = Label(window_silver_hall, text="Menu A", font=15, fg="blue")
menuA.grid(row=2, column=0)
menuB = Label(window_silver_hall, text="Menu B", font=15, fg="blue")
menuB.grid(row=2, column=5)
menuC = Label(window_silver_hall, text="Menu C", font=15, fg="blue")
menuC.grid(row=2, column=50)

menuA = Label(window_silver_hall, text="Menu A", font=15, fg="blue")
menuA.grid(row=2, column=0)
menuB = Label(window_silver_hall, text="Menu B", font=15, fg="blue")
menuB.grid(row=2, column=5)
menuC = Label(window_silver_hall, text="Menu C", font=15, fg="blue")
menuC.grid(row=2, column=50)

menuA1 = Label(window_silver_hall, text="Welcome drink", font=15,)
menuA1.grid(row=3, column=0)
menuA2 = Label(window_silver_hall, text="White Rice", font=15,)
menuA2.grid(row=4, column=0)
menuA3= Label(window_silver_hall, text="Yellow Rice", font=15,)
menuA3.grid(row=5, column=0)
menuA4= Label(window_silver_hall, text="Fried Rice", font=15,)
menuA4.grid(row=6, column=0)
menuA5 = Label(window_silver_hall, text="Devel Chicken", font=15,)
menuA5.grid(row=7, column=0)
menuA6 = Label(window_silver_hall, text="Devel Cuttle Fish ", font=15,)
menuA6.grid(row=8, column=0)
menuA7= Label(window_silver_hall, text="Devel Fish", font=15,)
menuA7.grid(row=9, column=0)
menuA8= Label(window_silver_hall, text="Fried Chicken Curry", font=15,)
menuA8.grid(row=10, column=0)
menuA9 = Label(window_silver_hall, text="Egg Salad", font=15,)
menuA9.grid(row=11, column=0)
menuA10 = Label(window_silver_hall, text="Brinjol Moju", font=15,)
menuA10.grid(row=12, column=0)
menuA11 = Label(window_silver_hall, text="Cachew Curry", font=15,)
menuA11.grid(row=13, column=0)
menuA12 = Label(window_silver_hall, text="Closlo Salad", font=15,)
menuA12.grid(row=14, column=0)
menuA13 = Label(window_silver_hall, text="Dhal Curry", font=15,)
menuA13.grid(row=15, column=0)
menuA13 = Label(window_silver_hall, text="Cuttlets & Papadam", font=15,)
menuA13.grid(row=16, column=0)
menuA14 = Label(window_silver_hall, text="Mousse", font=15,)
menuA14.grid(row=17, column=0)
menuA15 = Label(window_silver_hall, text="Watalppan", font=15,)
menuA15.grid(row=18, column=0)
menuA16 = Label(window_silver_hall, text="Ice Cream", font=15,)
menuA16.grid(row=19, column=0)
menuA17 = Label(window_silver_hall, text="Jelly", font=15,)
menuA17.grid(row=20, column=0)
menuA18 = Label(window_silver_hall, text="Ice Coffee", font=15,)
menuA18.grid(row=21, column=0)

menuB1 = Label(window_silver_hall, text="Welcome Drink", font=15,)
menuB1.grid(row=3, column=5)
menuB2 = Label(window_silver_hall, text="White Rice", font=15,)
menuB2.grid(row=4, column=5)
menuB3 = Label(window_silver_hall, text="Fried Rice", font=15,)
menuB3.grid(row=5, column=5)
menuB4 = Label(window_silver_hall, text="Noodles", font=15,)
menuB4.grid(row=6, column=5)
menuB5 = Label(window_silver_hall, text="Devel Fish", font=15,)
menuB5.grid(row=7, column=5)
menuB6 = Label(window_silver_hall, text="Fried Chicken Curry", font=15,)
menuB6.grid(row=8, column=5)
menuB7 = Label(window_silver_hall, text="Egg Salad", font=15,)
menuB7.grid(row=9, column=5)
menuB8 = Label(window_silver_hall, text="Cachew Curry", font=15,)
menuB8.grid(row=10, column=5)
menuB9 = Label(window_silver_hall, text="Achcharu", font=15,)
menuB9.grid(row=11, column=5)
menuB10 = Label(window_silver_hall, text="Ice Coffee", font=15,)
menuB10.grid(row=21, column=0)
menuB11= Label(window_silver_hall, text="Dhal Curry", font=15,)
menuB11.grid(row=12, column=5)
menuB12= Label(window_silver_hall, text="Cutlets & Papadam", font=15,)
menuB12.grid(row=13, column=5)
menuB13 = Label(window_silver_hall, text="Puddin", font=15,)
menuB13.grid(row=14, column=5)
menuB14 = Label(window_silver_hall, text="Watalappan", font=15,)
menuB14.grid(row=15, column=5)
menuB15 = Label(window_silver_hall, text="Ice Cream", font=15,)
menuB15.grid(row=16, column=5)
menuB16 = Label(window_silver_hall, text="Fruits", font=15,)
menuB16.grid(row=17, column=5)
menuB17 = Label(window_silver_hall, text="Custud", font=15,)
menuB17.grid(row=17, column=5)
menuB18 = Label(window_silver_hall, text="Ice Cream", font=15,)
menuB18.grid(row=18, column=5)
menuB19 = Label(window_silver_hall, text="Jelly", font=15,)
menuB19.grid(row=19, column=5)
menuB20 = Label(window_silver_hall, text="Ice Coffee", font=15,)
menuB20.grid(row=20, column=5)

menuC1 = Label(window_silver_hall, text="Welcome drink", font=15,)
menuC1.grid(row=3, column=50)
menuC2 = Label(window_silver_hall, text="White Rice", font=15,)
menuC2.grid(row=4, column=50)
menuC3 = Label(window_silver_hall, text="Yellow Rice", font=15,)
menuC3.grid(row=5, column=50)
menuC4= Label(window_silver_hall, text="Fried Rice", font=15,)
menuC4.grid(row=6, column=50)
menuC5 = Label(window_silver_hall, text="Fried Chicken Curry", font=15,)
menuC5.grid(row=7, column=50)
menuC6 = Label(window_silver_hall, text="Fish Curry", font=15,)
menuC6.grid(row=8, column=50)
menuC7 = Label(window_silver_hall, text="Egg Salad", font=15,)
menuC7.grid(row=9, column=50)
menuC8 = Label(window_silver_hall, text="Brinjol Salad", font=15,)
menuC8.grid(row=10, column=50)
menuC9 = Label(window_silver_hall, text="Potatoes", font=15,)
menuC9.grid(row=11, column=50)
menuC10 = Label(window_silver_hall, text="Cachew Curry", font=15,)
menuC10.grid(row=12, column=50)
menuC11 = Label(window_silver_hall, text="Dhal Curry", font=15,)
menuC11.grid(row=13, column=50)
menuC12 = Label(window_silver_hall, text="Vegetable Salad", font=15,)
menuC12.grid(row=14, column=50)
menuC13 = Label(window_silver_hall, text="Culets & Papadam", font=15,)
menuC13.grid(row=15, column=50)
menuC14 = Label(window_silver_hall, text="Ice Cream", font=15,)
menuC14.grid(row=16, column=50)
menuC15 = Label(window_silver_hall, text="Jelly", font=15,)
menuC15.grid(row=17, column=50)
menuC16 = Label(window_silver_hall, text="Watalappan", font=15,)
menuC16.grid(row=18, column=50)
menuC17 = Label(window_silver_hall, text="Fruit salad", font=15,)
menuC17.grid(row=19, column=50)
menuC = Label(window_silver_hall, text="Ice Coffee", font=15,)
menuC.grid(row=20, column=50)

menuBp1 = Label(window_silver_hall, text="Plate = Rs5000.00", font=15, fg="green")
menuBp1.grid(row=35, column=0)
menuBp2 = Label(window_silver_hall, text="Plate = Rs3000.00", font=15, fg="green")
menuBp2.grid(row=35, column=5)
menuBp3 = Label(window_silver_hall, text="Plate = Rs2000.00", font=15, fg="green")
menuBp3.grid(row=35, column=50)

exit_button = Button(window_silver_hall, text="Exit", command=exit, font=12, fg="white", bg="gray")
exit_button.grid(row=45, column=3)
next_button = Button(window_silver_hall, text="Next", font=12, command=page5, fg="white", bg="gray")
next_button.grid(row=45, column=6)

window_silver_hall.mainloop()