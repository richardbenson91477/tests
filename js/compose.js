#!/usr/bin/env jsc

// from Jim Weirich, "Adventures in Functional Programming"

print (function() {
    var make_adder = function (x) {
        return function (n) { 
            return n + x 
        }
    }
 
    var compose = function (f, g) {
        return function (n) {
            return f (g (n))
        }
    }
 
    var add1 = make_adder (1)
    var mul3 = function (n) {
        return n * 3
    }
    
    var mul3add1 = compose (mul3, add1)
 
    return mul3add1 (10)
}()
)

