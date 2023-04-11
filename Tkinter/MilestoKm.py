import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("400x250")
window.title("MilestoKms")

def convert():
    miles = entryint.get()
    km = miles * 1.61
    output_String.set(km)


title_label = ttk.Label(text="Miles to Km's",font="calbiri 30",master=window)
title_label.pack()


input_frame = ttk.Frame(master=window)
entryint = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entryint)
button = ttk.Button(master=input_frame, text="convert", command=convert)
entry.pack(side="left")
button.pack(side="left")
input_frame.pack(pady=10)

output_String = tk.StringVar()
output_label = ttk.Label(master=window, text = "ne", textvariable=output_String, font="calbiri 20")
output_label.pack()










window.mainloop()