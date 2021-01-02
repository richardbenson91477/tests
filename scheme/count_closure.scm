(define c 4)

(let* (
      (c 0)
      (my_count
        (lambda ()
          (set! c (+ c 1))
          (display c)
          (newline)
        )
      )
    )
  (my_count)
  (my_count)
)

(let (
      (c 0)
      (my_count
        (lambda ()
          (set! c (+ c 1))
          (display c)
          (newline)
        )
      )
    )
  (my_count)
  (my_count)
)
 
