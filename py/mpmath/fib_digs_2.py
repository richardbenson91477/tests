#!/usr/bin/env python3
# c/o https://www.goldennumber.net/five-phi/
from mpmath import mp
from sys import argv
from math import ceil
    
def main():
    argc = len(argv)
    if argc < 2:
        print ("usage: " + argv[0] + " start [stop [step]]\n")
        return
    else:
        r1 = int(argv[1])
        r2 = r1 + 1
        r3 = 1
        if argc >= 3:
            r2 = int(argv[2])
        if argc >= 4:
            r3 = int(argv[3])
 
    for n_d in range(r1, r2, r3):
        mp.dps = 16 if n_d < 16 else n_d + int(mp.log10(n_d)) + 1;
        n = ceil(n_d * 4.78497196678167 - 3.11269602859711)
        fib = int(mp.fib(n))
        print(str(n).ljust(4), fib)

if __name__ == '__main__':
    main()

