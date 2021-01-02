default(realprecision, 16)

f = 3*x^2*y - y^3 - 3*x^2 -3*y^2;
print("f=", f);

dfx = deriv(f, x);
dfy = deriv(f, y);
print("dfx=", dfx, "\ndfy=", dfy);

ddfx = deriv(dfx, x);
ddfy = deriv(dfy, y);
dfxy = deriv(dfx, y);
print("ddfx=", ddfx, "\nddfy=", ddfy, "\ndfxy=", dfxy);

/* stuck here - no nonlinear system solver */
/* 
sdf = solve((dfx, dfy), (x, y));
*/

