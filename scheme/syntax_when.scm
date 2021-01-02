
(define-syntax my_when
  (syntax-rules ()
    ((_ pred b1 ...)
      (if pred (begin b1 ...))
    )
  )
)

(my_when #t (display "tru") (display "e"))
(my_when #f (display "fal") (display "se"))
(newline)

