! c/o https://stackoverflow.com/questions/4070528/
program array1
  implicit none
  integer i, j
  real :: a(3,3) = reshape([((real(i) / real(j), i = 1, 3), j = 1, 3)], [3, 3])
  print *, a
end

