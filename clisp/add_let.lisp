#!/usr/bin/sbcl --script

(format t "~d~%"
    (let
        ((x (lambda (a b)
            (+ a b)))) 
      (funcall x 3 4)
    )
)

