#!/usr/bin/env python3
# c/o https://www.goldennumber.net/five-phi/
from mpmath import mp
from sys import argv
    
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
        
    mp.dps = 16
    φ = (1.0 + mp.sqrt(5.0)) / 2.0
    inv_log10_φ = 1.0 / mp.log10(φ)
    log10_5_d2_m1_t_inv_log10_φ = ((mp.log10(5.0) / 2.0) - 1.0) * inv_log10_φ

    for n_d in range(r1, r2, r3):
        mp.dps = 16
        # c/o https://www.geeksforgeeks.org/finding-number-of-digits-in-nth-fibonacci-number/
        # rearrange to find fib n of n_d digits
        # n_d = n * mp.log10(φ) - (mp.log10(5.0) / 2.0)
        # n * mp.log10(φ) = n_d + (mp.log10(5.0) / 2.0)
        # n = (n_d + (mp.log10(5.0) / 2.0)) / mp.log10(φ)
        # .. yet ceil (vs floor or nint) and (n_d - 1) give the best result (?)
        # n = int(mp.ceil((n_d - 1 + log10(5)_d2) / log10_φ))
        # n = int(mp.ceil((n_d + log10(5)_d2_m1) * inv_log10_φ))
        n = int(mp.ceil(n_d * inv_log10_φ + log10_5_d2_m1_t_inv_log10_φ))

        mp.dps = 16 if n_d < 16 else n_d + int(mp.log10(n_d)) + 1;
        fib = int(mp.fib(n))
        n_d_calc = 1 + int(mp.nint(mp.log10(fib)))
        if (n_d_calc != n_d):
            print(f"\nalgorithm error at {n_d_calc} != {n_d}")
            break
        print(str(n).ljust(4), fib)

if __name__ == '__main__':
    main()

