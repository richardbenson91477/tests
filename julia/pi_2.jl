#!/usr/bin/env julia 

function find_pi()
    num_steps = 10 ^ 9
    step = 1.0 / num_steps

    total = 0.0
    for i ∈ 1:num_steps
        total += 4.0 / (1.0 + ((i + 0.5) * step)^2)
        end

    return step * total
end

pi_valid = 3.141592653589793238
pi = find_pi()
print(pi, " ", pi_valid, "\n")

