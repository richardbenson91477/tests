package main

import (
	"fmt"
)

func main() {
    fmt.Printf("hey Go, does (0.7 + 0.2) + 0.1 equal 0.7 + (0.2 + 0.1)?\n")

    b := ((0.7 + 0.2) + 0.1) == (0.7 + (0.2 + 0.1))
    fmt.Printf("%v\n", b)

    if !b {
        fmt.Printf("womp womp womp\n")
    } else {
        fmt.Printf("You got it!\n")
    }
}

