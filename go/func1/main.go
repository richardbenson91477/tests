package main
import "fmt"

func main () {
    add3 := func (x int) int {
        return 3 + x
    }

    fmt.Printf("%v\n", add3(4))

    make_adder := func (x int) func (int) int {
        return func (y int) int {
            return x + y
        }
    }

    add4 := make_adder(4)
    fmt.Printf("%v\n", add4(3))

    fmt.Printf("%v\n", make_adder(5)(2))

    func () {
        fmt.Printf("adios\n");
    } ()
}

