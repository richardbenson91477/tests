
(display
  ; call/cc returns 11 because k is not applied to any argument
  (* 2 (call/cc (lambda (k) (+ 10 1)))))
(newline)

(display
  ; call/cc returns 1 because k is applied to 1 causing it to return immediately
  (* 2 (call/cc (lambda (k) (+ 10 (k 1))))))
(newline)

