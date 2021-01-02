! c/o http://web.stanford.edu/class/me200c/tutorial_77/
program main
  implicit none
  real :: a(2) = [1.0, 2.0], c(2)
  real :: b(2) = [3.0, 4.0]

  print *, a
  print *, b
  call saxpy(2, 1.0, a, b, c)
  print *, c
end program main
 
! saxpy: Compute y := alpha*x + y,
!   where x and y are vectors of length n (at least).
subroutine saxpy (n, alpha, x, y, res)
  implicit none
  integer, intent(in) :: n
  real, intent(in) :: alpha, x(n), y(n)
  real, intent(out) :: res(n)
  integer i

  res = [(alpha * x(i) + y(i), i = 1, n)]
  return
end subroutine saxpy

