#!/usr/bin/env jsc

var pi_valid = 3.141592653589793238
var num_steps = 1e+08
var step = 1.0 / num_steps

var total = 0.0
for (var i = 0; i < num_steps; i ++) {
    x = (i + 0.5) * step
    total += 4.0 / (1.0 + x * x)
}
var pi = step * total

print (pi, " ", pi_valid, "\n")

