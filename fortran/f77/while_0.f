c c/o http://web.stanford.edu/class/me200c/tutorial_77/
      program while0
      implicit none
      integer n
      n = 1
  10  if (n <= 10) then
        write (*,*) n
        n = 2 * n
        goto 10
      endif
      stop
      end

