#!/usr/bin/sbcl --script

(setq x 0.0)
(loop 
    (print x)
    (format t "~%" )
    (setq x (+ x 0.1))
    (if (> x 1.0) (return))
)

