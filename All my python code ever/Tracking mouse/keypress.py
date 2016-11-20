a=0
while a< 100:
    a=a+1
    win32api.keybd_event(67,0,0,0)
    win32api.keybd_event(67,0,2,0)
    ##time.sleep(0.5)

    #this code simulates a key event. first arg is the imortant one, tells you number of the key (this one is c)
    # see https://gist.github.com/chriskiehl/2906125  very useful.  the third agr tells the key to be released if 2, by default it is pressed.
