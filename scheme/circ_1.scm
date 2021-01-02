(map 
  (lambda (x)
    (display 
      (cos x)
    )
    (display " ")
    (display 
      (sin x)
    )
    (newline)
  )
  (map 
    (lambda (y) 
      (/ y 100)
    ) 
    (iota 628)
  )
)

