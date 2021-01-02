#!/usr/bin/env jsc

var s = JSON.parse (read ("./s.json"));

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

