from tkinter import *
from tkinter import ttk
from signaller import MorseTimer
from morse_coder import decode_word

# GUI Setup
root = Tk()

frm = ttk.Frame(root, padding=20)
frm.grid(padx=10,pady=10)

# Selected WPM and Morse Code Timer setup
selected_wpm = IntVar()
selected_wpm.set(10)
morse_timer = MorseTimer(selected_wpm.get())

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
wpm_scale = ttk.Scale(frm, from_=5, to=60, orient=HORIZONTAL, variable=selected_wpm,command=update_wpm)
wpm_scale.grid(column=1,row=1, padx=25)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)

# Can't use TKinter mainloop() since need to check for Arduino communication in realtime as well
while True:
    # Check for keys
    if morse_timer.is_active():
        new_word = morse_timer.tick()
        if new_word != "":
            TODO("GRAB WORD AND DUMP RAW INSIDE RAW INPUT, TRANSLATE AND DUMP IN TRANSLATED INPUT")
    root.update()