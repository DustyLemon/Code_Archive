
#To improve, i need to make it so random events kill the proportion of killers too#
import random,tkinter,time
from countries import *
Natural_disaster_chance = int(input("From 0-100, how disaster prone is this place?"))
Simulation_length = int(input("How long are we simulating for?"))
Bloodthirstyness_of_killers = int(input("From 0-100, how bloodythirsty are your killers?"))
country = input("Insert your country")
title = [" An earthquake","a whirlpool","A meteorite shower","A lemon party","A JewRoach","Pneumonic plague", "A Volcano"," Reconnection failure", "9/11*1000", "A lesbian death march", "A Russian peacekeeping mission","A dirty bomb","A tsunami","A Pucy zombie apocolypse","A wild chair", "My schlong"] 
message = "Oh the humanity! Suprisingly frequent and generic natural disaster kills hundreds."

def simulation(Birthrate_per_person_per_day,percentage_of_pop_killers,Civ_Population,Killer_Population):
    day = 0
    print("Day 0")
    print("civs:" , Civ_Population)
    print("killers:" , Killer_Population)
    while day < Simulation_length:
        Natural_disaster_death_count = random.randint(100, 900)
        time.sleep(1)
        day = day + 1
        print("Day",day)
        if random.random() <= (Natural_disaster_chance/100) :       
            tkinter.messagebox.showinfo(random.choice(title) + " has struck Theotopia" , message)
            if Civ_Population < Natural_disaster_death_count: 
                print("SO MANY DEATHS:", Civ_Population)
                Civ_Population = 0
            else:
                Civ_Population = Civ_Population - Natural_disaster_death_count
                print("SO MANY DEATHS:" , Natural_disaster_death_count) 
            
        
        for x in range(0, Civ_Population):
            if random.random() <= Birthrate_per_person_per_day:
                if random.random() <= (percentage_of_pop_killers/100):
                    Killer_Population = Killer_Population + 1
                else:
                    Civ_Population = Civ_Population + 1


        for x in range(0, Killer_Population):
            total_minus_thatguy = Civ_Population + Killer_Population - 1
            if Killer_Population == 1 and Civ_Population == 0:
                print(" Yay steve wins")
            elif random.random() <= (Bloodthirstyness_of_killers/100):            
                if Civ_Population != 0:
                    if random.random() <= Civ_Population/total_minus_thatguy:
                        Civ_Population = Civ_Population - 1
                    else:
                        Killer_Population = Killer_Population - 1
                else:
                    Killer_Population = Killer_Population - 1
   
                        



        print("civs:" , Civ_Population)
        print("killers:" , Killer_Population)

    print('Total civs:',Civ_Population)
    print('Total killers:',Killer_Population)


simulation([country]["Birthrate_per_person_per_day"],[country]["percentage_of_pop_killers"],[country]["Civ_Population"],[country]["Killer_Population"])

