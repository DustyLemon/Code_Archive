from time import *
import msvcrt
state = 0
health = 100
def keypress(wait_time, key):
    current_time = time()
    while current_time +wait_time > time() :
        if msvcrt.kbhit():
            if msvcrt.getwch() == key:
                global state
                state = 1
                break




print(' PRESS r TO READ THE GAME RULES OR IGNORE TO PROCEED')
#keypress(3,'r')
#if state == 1:
    #print rules
print('\n')
state = 0

print('\'So, which school did you come from? Belfast, ahh, that\'s cool. I was just in Ireland recently myself.\'')
sleep(3)
print('\n\n\'Sorry, what\'s your name again? I really am aweful with names.\'')
protag_name = input('')
print('\'Ahh yes, of course, ' + protag_name +', silly me\' ')
print('PRESS q TO ASK HIS NAME')
keypress(5,'q')
if state == 1:
    print('\'I\'m Theo, I\'ll be showing you around all our lessons I guess.\' He looked down at his timetable. \'Fuck, English. Dammit. It\'s this way\'')
    sleep(3)
else:
    print('He looked down at his timetable. \'Fuck, English. Dammit. It\'s this way\'')
    sleep(3)
state = 0
print('The hallway is packed, seas of children trying to get to their lessons. Suddenly, a scrawny year seven, struggling to get his bag off the top of a locker, accidently knocks over a cricket bat laying perched precariously over the edge.\'')
sleep(7)
print('PRESS d TO DODGE')
keypress(0.65,'d')
if state == 1:
      sleep(0.6)
      print('You quickly avoided the flying cricket bat, narrowly avoiding unitentional face surgery')  
      sleeep(2)  
      print('\'Ha, nice duck, you gotta watch out for the little shitheads everywhere\'')
else:
      health = health - 1
      print('The cricket bat whacks you on the cheek')
      sleep(2)
      print('\' Ouch, that\'s gonna leave a mark\'')
      sleep(2)
      print('HEALTH:'+ str(health))
sleep(2)
print('\' Come on, we\'d better get to English\'')

