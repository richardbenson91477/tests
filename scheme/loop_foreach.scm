
(for-each
  (lambda (c)
    (display c)
    (newline)
  )
  (map 1+ (iota 12))
)

