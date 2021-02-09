(display "Hey guile, does (0.7 + 0.2) + 0.1 equal 0.7 + (0.2 + 0.1)?")
(newline)

(let ((x (= (+ (+ 0.7 0.2) 0.1) (+ 0.7 (+ 0.2 0.1)))))
  (display x)
  (newline)
  (if x
      (display "Good job!")
      (display "womp womp")
  )
  (newline)
)
