program main
  implicit none
  real a(2,2), b(2,1), ipiv(2)
  integer info

! 3 * x + y = 9
! x + 2 * y = 8
  a(:,1) = (/3.0, 1.0/)
  a(:,2) = (/1.0, 2.0/)
  b(1,:) = 9.0
  b(2,:) = 8.0

  print *, 'a(:,1) = ', a(:,1)
  print *, 'a(:,2) = ', a(:,2)
  print *, 'b = ', b

  call sgesv(2, 1, a, 2, ipiv, b, 2, info)
  print *, 'sgesv -> b = ', b

  stop
end program
 
