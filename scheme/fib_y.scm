
(define (Y f) (
    (lambda (s) (s s))
    (lambda (s)
      (f (lambda (arg)
        ((s s) arg))
      )
    )
  )
)

(display (
    (Y
      (lambda (s)
        (lambda (n)
          (cond 
            ((= n 0) 1) 
            ((= n 1) 1)
            (else (+ (s (- n 1)) (s (- n 2))))
          )
        )
      )
    )
    33
  )
)
(newline)

