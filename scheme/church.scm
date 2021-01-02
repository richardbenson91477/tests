; numerals
(define @0
  (lambda (f)
    (lambda (x) x)
  )
)

(define @1
  (lambda (f)
    (lambda (x)
      (f x)
    )
  )
)

(define @2
  (lambda (f)
    (lambda (x)
      (f (f x))
    )
  )
)

; arithmetic
(define @1+
  (lambda (n)
    (lambda (f)
      (lambda (x)
        (f ((n f) x))
      )
    )
  )
)

(define @+
  (lambda (a)
    (lambda (b)
      (lambda (f)
        (lambda (x)
          ((a f) ((b f) x))
        )
      )
    )
  )
)

; logic
(define @t
  (lambda (f)
    (lambda (x) f)
  )
)

(define @f
  (lambda (f)
    (lambda (x) x)
  )
)


