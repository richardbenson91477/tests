package main

import (
	"fmt"
)

// a way to estimate π
func main() {
    const pi_valid = 3.141592653589793238
	const num_steps = 1_000_000_000
	const step = 1.0 / float64(num_steps)

	total := 0.0
	for i := 0; i < num_steps; i++ {
		// 0.5 for "midpoint Riemann sum"
        x := (float64(i) + 0.5) * step
		total += 4.0 / (1.0 + x*x)
	}
	pi := step * total

	fmt.Printf("%.16f %.16f\n", pi, pi_valid)
}

