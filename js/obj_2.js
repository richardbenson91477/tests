#!/usr/bin/env jsc

var obj2 = function (n) {
    var print_obj2 = function () {
        print (this.name + ' ' + this.color)
    }

    return {
        "name":n,
        "color":"red",
        "print":print_obj2
    }
}

var main = function () {
    var po = new obj2 ("joe")
    po.print ()
    po.name = "fred"
    var po2 = new obj2 ("john")
    po2.print ()
    po.print ()
}

main ()

