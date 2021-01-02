
(display
  (let next 
      ((n 0))
    (if (= n 10)
      (cons n '())
      (cons n (next (+ n 1)))
    )
  )
)
(newline)

