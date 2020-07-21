#!/usr/bin/python
from tkinter import *


main = Tk()
main.title('My cool new window!')
main.geometry('500x500')
# defines Button 2 and places it using grid
button2 = Button(main, text='23Filter Pump')
button2.grid(row=2, column=5)

# defines Button 1 and places it using grid
button1 = Button(main, text='Heading')
button1.grid(row=3, column=9, columnspan=4, rowspan=3)

# defines Button 2 and places it using grid
button2 = Button(main, text='Filter Pump')
button2.grid(row=1, column=8)

# defines Button 3 and places it using grid
button3 = Button(main, text='Rover Pump')
button3.grid(row=2, column=3)

# defines Button 4 and places it using grid
button4 = Button(main, text='Floodlight Pool')
button4.grid(row=4, column=3)

main.mainloop()