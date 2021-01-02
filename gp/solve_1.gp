/* 3 * x + y = 9
   x + 2 * y = 8 */
a = [3, 1; 1, 2];
x = matsolve(a, [9, 8]~);
print(x)

