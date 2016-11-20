__author__ = 'Theo'

import win32api
import time
import random
import win32con


def keypress(char):
    win32api.keybd_event(win32api.VkKeyScan(char), 0, 0, 0)

def type_string(string):
    time.sleep(2)
    for character in string:
        time.sleep(random.uniform(0.03, 0.5))
        keypress(character)
def make_new_file(name):
    time.sleep(0.5)
    win32api.keybd_event(0x12, 0, 0, 0)
    win32api.keybd_event(0x2D, 0, 0, 0)
    win32api.keybd_event(0x2D, 0, 2, 0)              # alt+insert
    win32api.keybd_event(0x12, 0, 2, 0)

    win32api.keybd_event(80, 0, 0, 0)
    win32api.keybd_event(80, 0, 2, 0)                  #p

    win32api.keybd_event(0x0D, 0, 0, 0)                #return
    win32api.keybd_event(0x0D, 0, 2, 0)

    type_string(name)

    win32api.keybd_event(0x0D, 0, 0, 0)                 #return
    win32api.keybd_event(0x0D, 0, 2, 0)

    time.sleep(0.5)
    win32api.keybd_event(0x10, 0, 0, 0)             #starts holdiing shift
    win32api.keybd_event(0x23, 0, 0, 0)
    win32api.keybd_event(0x23, 0, 2, 0)             #goes to end
    win32api.keybd_event(0x10, 0, 2, 0)             #stops holding shift
    time.sleep(0.5)
    win32api.keybd_event(0x08, 0, 0, 0)
    win32api.keybd_event(0x08, 0, 2, 0)             #backspaces


#make_new_file('test')
#type_string('pttcsst()')