
(display (
    (
      (lambda (s)
        (lambda (n)
          (if (zero? n)
            1
            (* n ((s s) (- n 1)))
          )
        )
      )
      (lambda (s)
        (lambda (n)
          (if (zero? n)
            1
            (* n ((s s) (- n 1)))
          )
        )
      )
    ) 
    10
  )
)
(newline)

