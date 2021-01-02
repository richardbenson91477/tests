c c/o http://web.stanford.edu/class/me200c/tutorial_77/
      program main
          real c
          write (*,*) r(2, 0.5)
      end 

      function r (m, t)
          integer m
          real t

          r = t * (m**2 + 2*m + 2)
          return
      end
