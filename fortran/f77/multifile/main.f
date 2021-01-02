c c/o http://web.stanford.edu/class/me200c/tutorial_77/
      program main
      integer m, n

      m = 1
      n = 2 

c   note the call by reference
      call iswap(m, n)
      write (*,*) m, n

      stop
      end

