
(define (omega f) (
    (lambda (x) (x x))
    (lambda (x) (f) (x x))
  )
)

(omega
  (lambda ()
    (display "y")
    (newline)
  )
)

