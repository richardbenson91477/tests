program main
  implicit none
  integer, parameter :: n = 4
  integer i
  real :: a(4) = [(real(i), i = 1, n)]
  real :: b(4) = [(0.0, i = 1, n)]

  print *, 'a = ', a
  print *, 'b = ', b

  print *, 'calling scopy (n, a, 1, b, 1)'
  call scopy(n, a, 1, b, 1)
  print *, 'b = ', b
end program
 
