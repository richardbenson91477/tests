#!/usr/bin/env julia

function find_root(fn, first_guess, err_eps, max_steps) 
    guess = first_guess

    dt = 1e-6

    steps = 0
    while true
        e = fn(guess)
        if abs(e) <= err_eps
            return guess, steps
        end

        d = (fn(guess + dt) - e) / dt

        guess = guess - (e / d)

        steps = steps + 1
        if steps > max_steps
            return guess, -1
        end

    end
end

fns = ((x -> x * x - 2.0, 1, "√2"),
       (x -> log(x) - 1, 1, "ℯ"),
       (x -> x * x - x - 1, 1, "φ"),
       (x -> sin(x), 3, "π"))

err_eps = 1e-14
max_steps = 50

for fn ∈ fns
    print(fn[3], ":")
    r, steps = find_root(fn[1], fn[2], err_eps, max_steps)
    if steps < 0
        print("(NOTE: reached max steps)")
    end

    print(r, " ", steps, " steps\n")
end

