c c/o http://web.stanford.edu/class/me200c/tutorial_77/
      program while1
      implicit none
      integer n
      data n /1/

      do while (n <= 10)
        write (*,*) n
        n = 2 * n
      enddo

      stop
      end

