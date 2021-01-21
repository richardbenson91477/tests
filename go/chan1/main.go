package main
import ("fmt"; "time")

func main () {
    done := make(chan int)
    go sayhi(done)
    <-done
}

func sayhi (done chan int) {
    for c := 0; c < 3; c ++ {
        fmt.Println("Hello, world!")
        time.Sleep(100_000_000)
    }
    done <- 1
}

