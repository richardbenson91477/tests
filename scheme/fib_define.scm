
(define (fib n)
  (cond 
    ((= n 0) 1)
    ((= n 1) 1) 
    (else (+ (fib (- n 1)) (fib (- n 2))))
  )
)

(display (fib 33))
(newline)

