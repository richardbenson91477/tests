package main
import (
    "fmt"
    "../add"
)

func main () {
    fmt.Printf("%v\n", add.Add3(add.Add4(0)))
}

