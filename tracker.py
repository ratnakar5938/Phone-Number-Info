import phonenumbers
import tkinter as tk
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


def getInformation(canvas):
    number = textField.get()
    ch_number = phonenumbers.parse(number, "CH")
    # print(geocoder.description_for_number(ch_number, "en"))

    service_number = phonenumbers.parse(number, "RO")
    # print(carrier.name_for_number(service_number, "en"))

    tz_number = phonenumbers.parse(number)
    # print(timezone.time_zones_for_number(tz_number))

    info = str(carrier.name_for_number(service_number, "en")) + "\n" + str(timezone.time_zones_for_number(tz_number))[2:-3]

    label1.config(text=str(geocoder.description_for_number(ch_number, "en")))
    label2.config(text=info)


canvas = tk.Tk()
canvas.geometry("600x300")
canvas.title("Phone Number Information")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getInformation)

label1 = tk.Label(canvas, font=t)
label1.pack()

label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
