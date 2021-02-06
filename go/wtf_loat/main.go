package main

import (
	"fmt"
)

// a way to estimate π
func main() {
    var c float64
	for c = 0.0; c <= 1.0; c += 0.1 {
	    fmt.Printf("%.16f\n", c)
    }

    if c != 1.0 {
        fmt.Printf("lol nope\n");
    }
}

