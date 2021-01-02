c c/o http://web.stanford.edu/class/me200c/tutorial_77/
      program do1
      implicit none
      integer i, a
 
      a = 0
      do 10 i = 1, 10
         a = a + i
         write(*,*) 'i =', i
         write(*,*) 'sum =', a
  10  continue

      stop
      end

