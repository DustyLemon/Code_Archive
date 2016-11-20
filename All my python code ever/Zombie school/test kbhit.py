from time import *
import msvcrt
state = 0
def keypress(wait_time, key):
    current_time = time()
    while current_time +wait_time > time() :
        if msvcrt.kbhit():
            if msvcrt.getwch() == key:
                global state
                state = 3
                break
keypress(3,'l')
print(state)
sleep(2)
