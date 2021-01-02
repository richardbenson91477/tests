#!/usr/bin/env jsc

print (
    (function (s) {
        return s (s)
      }
    )
    (function (s) {
        return function (n) {
          if (n == 0 || n == 1) return 1
          else return (s (s))(n - 1) + (s (s))(n - 2)
        }
      }
    )
    (33)
)

