from time import *
import msvcrt
var = time()
state = 0
while var +3 > time() :
    if msvcrt.kbhit():
        if msvcrt.getwch() == 'a':
            state = 1
            break

if state == 1:
    print('stab to te face')
else:
    print('Take it like a ma')
