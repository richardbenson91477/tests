#!/usr/bin/env python3
import sys

def imults (c, n):
    njust = len(str(c * n))
    for i in range(n):
        print(str(c * (i + 1)).rjust(njust))
    print()

def main ():
    if len(sys.argv) < 3:
        print ("usage: " + sys.argv[0] + " i n\n")
        return

    imults (int(sys.argv[1]), int(sys.argv[2]))

main()

