
(letrec (
      (nums
        (lambda (n)
          (cons n 
            (delay
              (nums (* n 2))
            )
          )
        )
      )
      (force-cdr
        (lambda (p)
          (force 
            (cdr p)
          )
        )
      )
    )
  (display
    (car (force-cdr (force-cdr (nums 1))))
  )
)

