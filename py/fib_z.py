#!/usr/bin/env python3
def main():
    (
      (lambda f:
        (lambda s:
          s(s))
        (lambda s: lambda n:
          f(s(s))(n))
      )
      (lambda s: lambda n: 
          print (1) or 1 if n == 0 else print (
            (lambda f:
              (lambda s:
                s(s)) 
              (lambda s: lambda n:
                f(s(s))(n))
            )
            (lambda s: lambda n:
              1 if n == 0 else (1 if n == 1 else s (n - 1) + s (n - 2))
            ) (n)
          ) or s (n - 1)
      )
    ) (30)

main()
