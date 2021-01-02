c c/o http://web.stanford.edu/class/me200c/tutorial_77/
      program array1
      implicit none
      real A(3,3)
      integer i, j

c     We will only use the upper 3 by 3 part of this array.

      do 20 j = 1, 3 ! you can do this for comments also
         do 10 i = 1, 3
            a(i,j) = real(i) / real(j)
   10    continue
   20 continue
        
      print *, a

      stop
      end

