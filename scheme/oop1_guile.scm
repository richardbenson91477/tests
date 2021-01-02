
(import (oop goops))

(define-class person () 
  (name #:init-keyword #:name #:accessor person-name)
  (age #:init-keyword #:age #:accessor person-age)
) 

(define-method (person-print (p person))
  (format #t "name: ~a age: ~a~%" (person-name p) (person-age p))
)

(define p 
  (list
    (make person #:name "Phil" #:age "10")
    (make person #:name "Jimmeny" #:age "20")
  )
)

(set! (person-name (car p)) "Jammeny")
;(slot-ref (car p) 'age)
(slot-set! (cadr p) 'age 30)

(map (lambda (pp) (person-print pp)) p)

