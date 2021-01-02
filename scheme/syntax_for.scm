
(define-syntax my_for 
  (syntax-rules ()
    ((_ (i from to) b1 ...)
      (let loop 
          ((i from))
        (if (< i to)
          (begin
            b1 ...
            (loop (+ i 1))
          )
        )
      )
    )
  )
)

(my_for (c 1 11)
  (display c)
  (newline)
)

