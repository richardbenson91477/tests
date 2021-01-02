#!/usr/bin/env jsc

// global state
var s = {
    "name": "tim",
    "number": 123,
    "area": 316
}

var main = function () {
    init ()
    return false
}

var init = function () {
    print ("hi, " + s.name)
    for (var y in s)
        print (y)
}

main ()

