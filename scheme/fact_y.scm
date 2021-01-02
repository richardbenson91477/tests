(define Y
  (lambda (f) (
      (lambda (s) (s s))
      (lambda (s)
        (f (lambda (arg)
          ((s s) arg))
        )
      )
    )
  )
)

(display (
    (Y
      (lambda (s)
        (lambda (n)
          (if (zero? n)
            1
            (* n (s (- n 1)))
          )
        )
      )
    )
    10
  )
)
(newline)

