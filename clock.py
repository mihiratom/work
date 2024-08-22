import tkinter as tk
import time

root = tk.Tk()
root.title("Clock")

clock = tk.Label(root, font=("times", 50, "bold"))
clock.pack()

def tick():

    now = time.strftime("%H:%M:%S")
    clock.config(text=now)
    clock.after(1000, tick)

tick()
root.mainloop()


