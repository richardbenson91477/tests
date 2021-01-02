(
  (
    (lambda (s) (s s))
    (lambda (s)
      (lambda (n)
        (if (< n 0.01)
          (display "Not enough bananas left!\n")
          (begin
            (display "You've ") (display n) (display " bananas. Eat how many? ") (
              (lambda (e)
                (if (< e 0) 
                  (begin 
                    (display "You can't negative eat!\n")
                    ((s s) n)
                  )
                  (if (< (- n e) 0)
                    (begin
                      (display "You can't eat more than you have!\n")
                      ((s s) n)
                    )
                    ((s s) (- n e))
                  )
                )
              ) 
              (read)
            )
          )
        )
      )
    )
  )
  30
)
