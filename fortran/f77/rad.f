c c/o http://web.stanford.edu/class/me200c/tutorial_77/
      program rad
      implicit none
      real r, pi
      parameter (pi = 3.1415926535897932384626)
 
      write (*,*) 'Give radius r:'
      read (*,*) r
      write (*,*) 'Area = ', pi * r ** 2
 
      stop
      end

