#!/usr/bin/env python3
import time

NITEMS=10_000_000
NRUNS=10

def test_append(n):
    l = []
    for x in range(n):
        l.append(x)

def test_plusequals(n):
    l = []
    for x in range(n):
        l += [x]

def main():
    print(f"running test_append {NITEMS} x {NRUNS}")
    init_time = time.time()
    for c in range(NRUNS):
        start_time = time.time()
        test_append(NITEMS)
        print("%s s" % (time.time() - start_time))
    print("total: %s s" % (time.time() - init_time))
    
    print(f"running test_plusequals {NITEMS} x {NRUNS}")
    init_time = time.time()
    for c in range(NRUNS):
        start_time = time.time()
        test_plusequals(NITEMS)
        print("%s s" % (time.time() - start_time))
    print("total: %s s" % (time.time() - init_time))

if __name__ == '__main__':
    main()
