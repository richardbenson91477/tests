
(let-syntax 
    ((nil! 
      (syntax-rules ()
        ((_ x)
          (set! x '())
        )
      )
    ))
  (define i 10)
  (display i)
  (newline)
  (nil! i)
  (display i)
  (newline)
)

