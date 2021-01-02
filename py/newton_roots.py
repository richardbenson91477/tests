#!/usr/bin/env python3
import math

def main():
    err_eps = 1e-14
    max_steps = 50

    fns = [[lambda x: x * x - 2.0, 1, '√2'],
            [lambda x: math.log(x) - 1, 1, 'ℯ'],
            [lambda x: x * x - x - 1, 1, 'φ'],
            [lambda x: math.sin(x), 3, 'π']
        ]

    for fn in fns:
        print(f"{fn[2]}:", end='')
        r, steps = find_root(fn[0], fn[1], err_eps, max_steps)
        if steps < 0:
            print("(NOTE: reached max steps)", endl='')

        print(f"{r}, {steps} steps")

def find_root (fn, first_guess, err_eps, max_steps):
    guess = first_guess

    dt = 1e-6

    steps = 0
    while True:
        e = fn(guess)
        if abs(e) <= err_eps:
            return guess, steps

        d = (fn(guess + dt) - e) / dt

        guess = guess - (e / d)

        steps = steps + 1
        if steps > max_steps:
            return guess, -1

main()

