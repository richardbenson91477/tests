package main

import (
	"fmt"
)

// for reference
const pi_valid = 3.141592653589793238

// a way to estimate π c/o https://www.youtube.com/watch?v=FQ1k_YpyG_A
func main() {
	const num_steps = 1000000000
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
