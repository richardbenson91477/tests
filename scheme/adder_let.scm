
(let* (
      (make-adder
        (lambda (a)
          (lambda (b) 
            (+ a b)
          ) 
        )
      )
      (add-one
        (lambda (a)
          ((make-adder a) 1)
        )
      )
  )
  (display (add-one 2))
  (newline)
  (display ((make-adder 2) 2))
  (newline)
)

