import tkinter as tk

counter = 0


def counter_label(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()
#def filter_pump()




root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)

button1 = tk.Button(root, text='Filter Pump', width=25, command=root.destroy)
# turns pump on or off, changes button colors, changes from 1 to 0,
button2 = tk.Button(root, text='Rover Pump', width=25, command=root.destroy)
# turns pump on or off, changes button colors, changes from 1 to 0,
button3 = tk.Button(root, text='Floodlight Pool', width=25, command=root.destroy)
# turns pump on or off, changes button colors, changes from 1 to 0,
button4 = tk.Button(root, text='Gate Lights', width=25, command=root.destroy)
# turns pump on or off, changes button colors, changes from 1 to 0,
button1.pack()
button2.pack()
button3.pack()
button4.pack()

button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()