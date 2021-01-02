#!/usr/bin/env jsc

var obj1 = function (name) {
   this.name = name
   this.color = "red"
}

obj1.prototype.print = function () {
    print (this.name + ' ' + this.color)
}

var main = function () {
    var po = new obj1 ("box1")
    po.print ()
    po.name = "box3"
    var po2 = new obj1 ("circle2")
    po2.print ()
    po.print ()
}

main ()

