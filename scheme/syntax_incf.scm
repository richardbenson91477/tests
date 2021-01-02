
(define-syntax incf 
  (syntax-rules () 
    ((_ x)
      (begin 
        (set! x (+ x 1))
        x
      )
    )
    ((_ x i)
      (begin 
        (set! x (+ x i)) 
        x
      )
    )
  )
)

(define i 0)
(define j 0)
(incf i)
(incf j 5)
(display i)
(newline)
(display j)
(newline)

