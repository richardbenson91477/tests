#!/usr/bin/env jsc

// from Jim Weirich, "Adventures in Functional Programming"

print (function() {
    var make_adder = x => n => n + x
    var compose = f => g => n => f(g(n))
    var add1 = make_adder(1)
    var mul3 = n => n * 3
    var mul3add1 = compose(mul3)(add1)
    return mul3add1(10)
}()
)

