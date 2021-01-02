
(display
  (filter even? '(9 10 11 21 22))
)
(newline)
(display
  (filter (lambda (x) (<= x 11)) '(9 10 11 21 22))
)
(newline)

