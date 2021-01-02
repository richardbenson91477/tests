; from wikipedia

(define (f return)
  (return 2)
  3)

; displays 3 because "return" is not a continuation
(display (f (lambda (x) x)))
(newline)
; displays 2 because "return" is a continuation
(display (call/cc f))
(newline)

