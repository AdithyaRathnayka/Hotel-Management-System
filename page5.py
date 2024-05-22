from tkinter import *
import tkinter.messagebox as MessageBox

window_last = Tk()
window_last.title("Royal reception hall")
window_last.geometry("750x400")


def save_data():
    first_name = textbox1.get()
    last_name = textbox2.get()
    contact_num = textbox3.get()
    Date = str(textbox4.get())
    selected_hall = (textbox6.get())
    num_of_plates = textbox5.get()
    cardnum = open("data.txt", "r")
    detailslist = []
    cardnumrecord = cardnum.readline()

    dateenter = Date
    hallenter = selected_hall
    while cardnumrecord:
        cardnumdata = cardnumrecord.strip().split(" : ")
        detailslist = detailslist + cardnumdata
        cardnumrecord = cardnum.readline()

    for i in range(len(detailslist)):
        if detailslist[i] == dateenter:
            if detailslist[i + 2] == hallenter:
               MessageBox.showinfo("This hall isn't available on this day")
               break
    else:
        print(first_name, last_name, contact_num, Date, selected_hall, num_of_plates)

        file = open("data.txt", "a")

        file.write("your first name : " + first_name)
        file.write("\n")
        file.write("your last name : " + last_name)
        file.write("\n")
        file.write("your contact number : " + contact_num)
        file.write("\n")
        file.write("your booking date : " + Date)
        file.write("\n")
        file.write("Hall you selected : " + selected_hall)
        file.write("\n")
        file.write("plates you want : " + num_of_plates)
        file.write("\n")
        file.close()


first_name = str()
last_name = str()
contact_num = str()
Date = str()
selected_hall = str()
num_of_plates = str()


def exit():
    window_last.destroy()


def bill_amount():
    selected_hall = textbox6.get()
    selected_menu = textbox7.get()
    num_of_seats = int(textbox5.get())

    if selected_hall == "Golden" and selected_menu == "A" and num_of_seats <= 1500:
        bill = int(num_of_seats)*8000
    elif selected_hall == "Silver" and selected_menu == "A" and num_of_seats <= 1000:
        bill = int(num_of_seats)*5000
    elif selected_hall == "Bronze" and selected_menu == "A" and num_of_seats <= 500:
        bill = int(num_of_seats)*3000
    elif selected_hall == "Golden" and selected_menu == "B" and num_of_seats <= 1500:
        bill = int(num_of_seats)*5000
    elif selected_hall == "Silver" and selected_menu == "B" and num_of_seats <= 1000:
        bill = int(num_of_seats)*3000
    elif selected_hall == "Bronze" and selected_menu == "B" and num_of_seats <= 500:
        bill = int(num_of_seats)*2000
    elif selected_hall == "Golden" and selected_menu == "C" and num_of_seats <= 1500:
        bill = int(num_of_seats)*3000
    elif selected_hall == "Silver" and selected_menu == "C" and num_of_seats <= 1000:
        bill = int(num_of_seats)*2000
    elif selected_hall == "Bronze" and selected_menu == "C" and num_of_seats <= 500:
        bill = int(num_of_seats)*1500
    else:
        bill = "Your requrement is not available"

    label_b = Label(window_last, text=bill, font=14, fg="green")
    label_b.grid(row=15, column=5)


label = Label(window_last, text="Royal Hall - Hall Reservation", font=20, fg="green")
label.grid(row=0, column=0)
label1 = Label(window_last, text="FirstName", font=14)
label1.grid(row=2, column=0)
label2 = Label(window_last, text="LastName", font=14)
label2.grid(row=3, column=0)
label3 = Label(window_last, text="Contact Number", font=14)
label3.grid(row=4, column=0)
label4 = Label(window_last, text="Date", font=14)
label4.grid(row=5, column=0)
label5 = Label(window_last, text="Quantity", font=14)
label5.grid(row=6, column=0)
label6 = Label(window_last, text="selected hall(Golden/Silver/Bronze)", font=14)
label6.grid(row=7, column=0)
label7 = Label(window_last, text="selected menu(A/B/C)", font=14)
label7.grid(row=8, column=0)


textbox1 = Entry(window_last, fg='blue')
textbox1.grid(row=2, column=1)
textbox2 = Entry(window_last, fg='blue')
textbox2.grid(row=3, column=1)
textbox3 = Entry(window_last, fg='blue')
textbox3.grid(row=4, column=1)
textbox4 = Entry(window_last, fg='blue')
textbox4.grid(row=5, column=1)
textbox5 = Entry(window_last, fg='blue')
textbox5.grid(row=6, column=1)
textbox6 = Entry(window_last, fg='blue')
textbox6.grid(row=7, column=1)
textbox7 = Entry(window_last, fg='blue')
textbox7.grid(row=8, column=1)

save_btn = Button(window_last, text="save", command=save_data, font=14, fg="white", bg="gray")
save_btn.grid(row=10, column=3)
bill_btn = Button(window_last, text="bill", command=bill_amount, font=14, fg="white", bg="gray")
bill_btn.grid(row=10, column=5)
exit_btn = Button(window_last, text="Exit", command=exit, font=14, fg="white", bg="gray")
exit_btn.grid(row=10, column=6)

window_last.mainloop()

