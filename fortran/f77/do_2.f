c c/o http://web.stanford.edu/class/me200c/tutorial_77/
      program do2
      implicit none
      integer i, a
 
      a = 0
      do i = 1, 10
         a = a + i
         write(*,*) 'i =', i
         write(*,*) 'sum =', a
      enddo

      stop
      end

