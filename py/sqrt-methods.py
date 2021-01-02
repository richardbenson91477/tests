#!/usr/bin/env python3
import math

method_names = ['newt', 'test']
methods_n = len(method_names)
method_newt, method_test = range(methods_n)

def main():
    eps = 1e-15
    max_steps = 50
    range_ = (0.2, 8.0, 0.2)

    x = range_[0]
    while x < range_[1]:
        for method in range(methods_n):
            r, steps = square_root(x, x / 3, eps, method, max_steps)
            if steps < 0:
                print(method_names[method], "error: too many steps")
            else:
                print(method_names[method], r, x, r * r, steps)
        x += range_[2]

def square_root(n, first_guess, eps, method, max_steps):
    guess = first_guess

    steps = 1
    while True:
        if method == method_newt:
            guess = (guess + (n / guess)) / 2.0
            e = n - (guess * guess)
        elif method == method_test:
            e = n - (guess * guess)
            guess = guess - (e / n)

        if abs(e) <= eps:
            return guess, steps

        steps = steps + 1
        if steps > max_steps:
            return guess, -1

main()
