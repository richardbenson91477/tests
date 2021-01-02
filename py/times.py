#!/usr/bin/env python3

def times (hm):
    for m in range(hm):
        for n in range(hm):
            print(str((m + 1) * (n + 1)).rjust (4), end='')
        print()

times (20)

