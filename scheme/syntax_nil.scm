
(define-syntax nil! 
  (syntax-rules ()
    ((_ x)
      (set! x '())
    )
  )
)

(define i 10)
(nil! i)
(display i)
(newline)
 
