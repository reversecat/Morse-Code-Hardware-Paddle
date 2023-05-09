from tkinter import *
from tkinter import ttk

root = Tk()

frm = ttk.Frame(root, padding=20)
frm.grid(padx=10,pady=10)

# Selected WPM
selected_wpm = IntVar()
selected_wpm.set(1)

# Slider Selected WPM event handler
def update_wpm(event):
    new_wpm = selected_wpm.get()
    wpm_label.configure(text="Selected WPM: " + str(new_wpm))

ttk.Label(frm, text="Translated Input").grid(column=0, row=0)
ttk.Frame(frm, padding=5, width=400, height=150, relief=SUNKEN).grid(column=0, row=1)

ttk.Label(frm, text="Raw Input").grid(column=0,row=2)
ttk.Frame(frm, padding=5, width=400, height=150, relief=SUNKEN).grid(column=0,row=3)

wpm_label = ttk.Label(frm, text="Selected WPM: " + str(selected_wpm.get()))
wpm_label.grid(column=1,row=0)
wpm_scale = ttk.Scale(frm, from_=1, to=100, orient=HORIZONTAL, variable=selected_wpm,command=update_wpm)
wpm_scale.grid(column=1,row=1, padx=25)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)

root.mainloop()