#!/usr/bin/env python3

def find_pi():
    num_steps = 10 ** 9
    step = 1.0 / num_steps

    total = 0.0
    for i in range(num_steps):
        total += 4.0 / (1.0 + ((i + 0.5) * step)**2)

    return step * total

def main():
    pi_valid = 3.141592653589793238
    pi = find_pi()
    print(pi, " ", pi_valid, "\n")

if __name__ == '__main__':
    main()
