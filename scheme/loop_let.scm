
(let count 
    ((a 1))
  (display a)
  (newline)
  (if (= a 10)
    #t
    (count (+ a 1))
  )
)

