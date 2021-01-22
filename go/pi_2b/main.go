package main

import (
	"fmt"
)

// a goroutines way to estimate π
func main() {
    const pi_valid = 3.141592653589793238
    const steps_n = 1_000_000_000
    const step = 1.0 / float64(steps_n)
    const t_n = 4
    const t_steps_n = steps_n / t_n

    t_chan := make(chan float64, t_n)

    for t_c := 0; t_c < t_n; t_c ++ {
        go func (i_begin int) {
            i_end := i_begin + t_steps_n

            total := 0.0
            for i := i_begin; i < i_end; i++ {
                // 0.5 for "midpoint Riemann sum"
                x := (float64(i) + 0.5) * step
                total += 4.0 / (1.0 + x*x)
            }
            t_chan <- total
        } (t_c * t_steps_n)
    }

    total := 0.0
    for t_c := 0; t_c < t_n; t_c ++ {
        total += <-t_chan
    }

	pi := step * total

	fmt.Printf("%.16f %.16f\n", pi, pi_valid)
}

