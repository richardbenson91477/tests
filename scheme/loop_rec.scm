
(define (disp_rec l)
  (if (null? l)
    #t
    (begin
      (display (car l))
      (newline)
      (disp_rec (cdr l))
    )
  )
)

(disp_rec (list 'a 'b 'c))

