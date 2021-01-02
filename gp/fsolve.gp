default(realprecision, 100)

r = solve(x=1,3, log(x) -1);
n = 1e+100;
s = (1 + 1/n) ^ n;
print("ℯ:\n", r, "\n", s, "\n")

r = solve(x=1,2, x^2 -x -1);
s = (1 + sqrt(5)) / 2;
print("φ:\n", r, "\n", s, "\n")

r = solve(x=3,4, sin(x));
s = Pi;
print("π:\n", r, "\n", s, "\n")

r = solve(x=0,2, x^2 - 2);
s = sqrt(2);
print("√2:\n", r, "\n", s, "\n")

