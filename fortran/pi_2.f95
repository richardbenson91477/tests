program main
  implicit none
  integer,parameter :: num_steps = 10 ** 9
  double precision,parameter :: pi_valid = 3.141592653589793238d0 ! note the d0
  double precision,parameter :: step = 1.0d0 / dble(num_steps)
  double precision :: x, total, pi
  integer :: i

  total = 0.0d0
  do i = 0, num_steps - 1
    x = (dble(i) + 0.5d0) * step
    total = total + 4.0d0 / (1.0d0 + x * x)
    !print *, x, total
  enddo

  pi = step * total
  print*, pi, pi_valid
end program

