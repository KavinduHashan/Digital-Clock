import tkinter as ui
import time

w = ui.Tk()
w.title("Digital CLock")

def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    AM_or_PM  = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + AM_or_PM
    digitalclock_lbl.config(text=time_text)
    digitalclock_lbl.after(1000, update_clock)

digitalclock_lbl = ui.Label(w, text="00.00.00",
                            font="Helvetica 72 bold",
                            bg="black",
                            fg="white")
digitalclock_lbl.pack()

update_clock()

w.mainloop()