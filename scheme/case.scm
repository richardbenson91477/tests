
(define (loop c)
  (if (= c 6)
    #t 
    (begin
      (display 
        (string-concatenate 
          `(,(number->string c)
          ,(case c
            ((0 1 2) " < 3\n")
            ((3) " = 3\n")
            (else " > 3\n")
          )
        ))
      )
      (loop (+ c 1))
    )
  )
)
(loop 1)

