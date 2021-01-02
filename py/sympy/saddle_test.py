#!/usr/bin/env python3
# c/o https://www.youtube.com/watch?v=TqslX-bUTD8&list=PLSQl0a2vh4HC5feHa6Rc5c0wbRTx56nF7&index=91
from sympy import *

x, y = symbols('x y')

fns = (x*x*x*x - 4*x*x + y*y,
        x*x + y*y + 4*x*y,
        3*x*x*y - y*y*y - 3*x*x -3*y*y)

for f in fns:
    print(f"f={f}")

    dfx = diff(f, x)
    dfy = diff(f, y)
    print(f"dfx={dfx}\ndfy={dfy}")
    
    ddfx = diff(dfx, x)
    ddfy = diff(dfy, y)
    dfxy = diff(dfx, y)
    print(f"ddfx={ddfx}\nddfy={ddfy}\ndfxy={dfxy}")

    sdf = solve((dfx, dfy), (x, y))
    if type(sdf) == dict:
        sdf = [(sdf[x], sdf[y])]
    print(f"sdf={sdf}")

    for s in sdf:
        sddfx = ddfx.subs([(x, s[0]), (y, s[1])])
        sddfy = ddfy.subs([(x, s[0]), (y, s[1])])
        sdfxy = dfxy.subs([(x, s[0]), (y, s[1])])
        H = sddfx * sddfy - sdfxy * sdfxy
        print(f"H({s[0]}, {s[1]})={H}")

    #plotting.plot3d(f, (x, -5, 5), (y, -5, 5))
    print()

