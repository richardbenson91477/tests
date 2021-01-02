#!/usr/bin/env python3
from tkinter import *
from math import sin, cos, pi
from time import sleep
from sys import exit
# derived from this reddit post:
# https://www.reddit.com/r/oddlysatisfying/comments/57iff3/the_lissajous_curve/

class s:
    ''' state '''
    win_w, win_h = (640, 480)
    win_hw, win_hh = (win_w // 2, win_h // 2)
    win = Canvas(Tk(), width=win_w, height=win_h)
    div_x = 15
    div_y = 14
    t_max = div_x * div_y * pi * 2
    step = 1.0

def pos (t):
    return (s.win_hw + s.win_hw * sin(t / s.div_x),
            s.win_hh + s.win_hh * cos(t / s.div_y))

def draw (t):
    p1 = pos(t)
    p2 = pos(t + s.step)
    s.win.create_line(p1[0], p1[1], p2[0], p2[1])

def main ():
    s.win.pack()
    t = 0.0
    while t <= s.t_max:
        draw(t)
        t += s.step
        s.win.update()
        sleep(0.01)

    print("done: hit enter")
    t = input()

    del(s.win)
    return(0)

if __name__ == "__main__":
    exit(main())

