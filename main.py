from tkinter import *


def miles_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.609)
    km_result.config(text=f"{km}")


window = Tk()
window.title("Miles to Km converter")
window.config(pady=60, padx=80)

title = Label(text="My First Program", font=("ariel", 20, "bold"))
title.config(pady=20, padx=0)
title.grid(column=2, row=0)

mile_input = Entry()
mile_input.grid(column=2, row=2)

label_mile = Label(text="Miles")
label_mile.grid(column=3, row=2)

is_equal = Label(text="is equal to")
is_equal.grid(column=2, row=3)

km_result = Label(text="0", font=("Ariel", 16, "bold"))
km_result.grid(column=2, row=4)

km_label = Label(text="Km")
km_label.grid(column=3, row=4)

btn = Button(text="calculate", command=miles_to_km)
btn.grid(column=2, row=5)

window.mainloop()
