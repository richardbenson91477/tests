#!/usr/bin/env python3

def main():
    print ((
        (lambda s: s (s))
        (lambda s: lambda n:
          1 if n == 0 or n == 1
          else (s (s))(n - 1) + (s (s))(n - 2)
        )
      ) (33))

main()
