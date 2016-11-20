import random
killer = 4
civies = 4
while killer != 0:
    print("No.killers:", killer)
    print("No.Civies:", civies)
    if random.random() <= 0.5 - (1/ killer + civies - 1)/100 :
        killer = killer - 1
    else:
        if civies == 0:
            killer = killer -1
        else:
            civies = civies -1
    
print(" Final No.killers:", killer)
print("Final No.Civies:", civies)

