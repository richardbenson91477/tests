package main
import "fmt"

func main () {
    var str string
    str += "Hello "
    str += "world! "
    fmt.Printf("%v %v\n", str, add3(4))
}

