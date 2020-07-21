# Pool Filter Pump Code

# Variables
volts = 230
amps = 7.5
hp = 1
rpm = 3450
wait = 5
Samantha = "Samantha"
link = ''
Program = "start"


# Beginning

while Program == "start":
    button = input("Name the button ")
    if button == "0" and wait == 5:
        if link != button:
            print("setLow")
        elif link == button:
            print('same_number')
        else:
            pass
        #link = button
    elif button == '1' and wait ==5:
        if link != button:
            print("setHigh")
        elif link == button:
            print('same_number')
        else:
            pass

    elif button != 0 or 1:
        if button == "x":
            Program = "stop"
        else:

            if link != button:
                print("no_change")
            elif link == button:
                print('same_number')
            else:
                pass
    link = button
    print("******************************************************")

print("out")





#input("Press Enter to start timer") # wait for the first Enter from the user
#start = timer()
#input("Press Enter to stop timer")
#elapsed = timer() - start