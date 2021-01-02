
(display (
    (
      (lambda (s) (s s))
      (lambda (s) 
        (lambda (n)
          (cond 
            ((= n 0) 1)
            ((= n 1) 1) 
            (#t (+ 
              ((s s) (- n 1))
              ((s s) (- n 2)))
            )
          )
        )
      )
    )
    33
  )
)

(newline)

