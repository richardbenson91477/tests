
(define-syntax my_while
  (syntax-rules ()
    ((_ pred b1 ...)
      (let loop ()
        (if pred
          (begin
            b1 ...
            (loop)
          )
        )
      )
    )
  )
)

(define c 1)

(my_while (< c 6)
  (display c)
  (newline)
  (set! c (+ c 1))
)

