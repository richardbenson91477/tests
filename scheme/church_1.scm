(load "./church.scm")

(define (pr-and-ret x)
  (display x)
  (newline)
  x
)

(
  (
    (@1+ @1) 
    (lambda (x)
      (pr-and-ret x)
    )
  )
  "two"
)

(
  (
    ((@+ @1) @2)
    (lambda (x) 
      (pr-and-ret x)
    )
  )
  "three"
)

