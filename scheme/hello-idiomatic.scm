
(let (
      (msg "Hello, world!")
    )
  (
    (lambda (x)
      (begin
        (display x)
        (newline)
      )
    )
    msg
  )
)

