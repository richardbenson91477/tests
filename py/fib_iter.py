#!/usr/bin/env python3
def main():
    last_n1 = 0
    last_n2 = 1
    for c in range (1,400):
        n = last_n1 + last_n2
        print(n)
        last_n2 = last_n1
        last_n1 = n
        # golden ratio: if last_n2: print("(" + str(n / last_n2) + ")")
main()
