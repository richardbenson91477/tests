#!/usr/bin/env python3
import time

def spawn_interact ():
    import threading
    def t_fun ():
        import code
        code.interact (local = locs)
    threading.Thread (target = t_fun).start ()

x = 1
locs = locals ()
spawn_interact ()
while (True):
    print (x)
    time.sleep (1); 

