#To improve, i need to make it so random events kill the proportion of killers too#
import random
import tkinter
import time
civs = int(input("How many civs in your society?"))
killers = int(input("How many killers in your society?"))
day = 0
title = [" An Earthquake","a Whirlpool","A Meteorite Shower","A Lemon Party","A JewRoach","Pneumonic plague", "A Volcano"," Reconnection failure", "9/11*1000", "A lesbian death march", "A Russian peacekeeping mission","A dirty bomb","A tsunami","A Pucy zombie apocolypse","A wild chair", "My schlong","Miss Griffiths's tits","SHINY GOLD X", "Extra purple","Viktor jungle",] 
message = "Oh the humanity! Suprisingly frequent and generic natural disaster kills hundreds."
while killers != 1 or civs != 0:
    # Add the option to add a day limit too#
    Natural_disaster_death_count = random.randint(100, 900)
    time.sleep(1)
    day = day + 1
    print("Day",day)
    if random.random() <= 0.00000000000001:       
        tkinter.messagebox.showinfo(random.choice(title) + " has struck Theotopia" , message)
        if civs < Natural_disaster_death_count: 
            print("SO MANY DEATHS:", civs)
            civs = 0
        else:
            civs = civs - Natural_disaster_death_count
            print("SO MANY DEATHS:" , Natural_disaster_death_count) 
            
        
    for x in range(0, civs):
        if random.random() <= 0.0000298908:
            if random.random() <=0.000140633:
                killers = killers + 1
            else:
                civs = civs + 1


    for x in range(0, killers):
        total_minus_thatguy = civs + killers - 1
        if random.random() <= 0.5:
            if civs != 0:
                if random.random() <= civs/total_minus_thatguy:
                    civs = civs - 1
                else:
                    killers = killers - 1
            else:
                killers = killers - 1
   
                        



    print("civs:" , civs)
    print("killers:" , killers)

print('Total civs:',civs)
print('Total killers:',killers)

time.sleep(2)
print ("Yay steve wins")

