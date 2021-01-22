package main

import "fmt"

var a struct {
	x int
}

type T struct {
	x int
}

var b T

type T2 struct {
	x int
}

func (t2 *T2) double() {
	t2.x *= 2
}

func main() {
	a.x = 3
	b = a
	c := T2(b)
	c.double()
	b = T(c)

	fmt.Printf("b = %v\n", b)
}

