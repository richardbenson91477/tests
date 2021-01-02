
(define n 30)
(define e 0)

(let main ()
  (display "You have ") (display n) (display " bananas. Eat how many? ")

  (set! e (read))

  (if (< e 0)
    (begin
      (display "You can't negative eat!")
      (newline)
    )
    (if (> e n) 
      (begin
        (display "You can't eat more than you have!")
        (newline)
      )
      (set! n (- n e))
    )
  )

  (if (< n 0.01)
    (begin
      (display "Not enough bananas left!")
      (newline)
    )
    (main)
  )
)

