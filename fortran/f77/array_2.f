c c/o http://web.stanford.edu/class/me200c/tutorial_77/
      program main
      implicit none
      real a(2), b(2), c(2)
      data a /1.0, 2.0/
      data b /3.0, 4.0/

      write (*,*) a
      write (*,*) b

      call saxpy(2, 1.0, a, b, c)

      write (*,*) c
      stop
      end program main
 
c   Saxpy: Compute y := alpha*x + y,
c   where x and y are vectors of length n (at least).
      subroutine saxpy (n, alpha, x, y, res)
      implicit none
      integer n
      real alpha, x(*), y(*), res(*)

      integer i

      do i = 1, n
         res(i) = alpha*x(i) + y(i)
      enddo

      return
      end subroutine saxpy

