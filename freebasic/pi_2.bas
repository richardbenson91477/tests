
var num_stps = 1e+9
var stp = 1.0 / num_stps
var stpsq = stp * stp
var pi = 3.141592653589793

var total = 0.0
for i as integer = 0 to num_stps
    if i mod 1e+8 = 0 then
        print i * 100 / num_stps; : print "%"
    end if 
    total = total + 4.0 / (1.0 + (i * i) * stpsq)

next i

var my_pi = stp * total
print my_pi, pi

print "pi - my_pi: ", pi - my_pi

