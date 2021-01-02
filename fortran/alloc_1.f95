program alloc
  implicit none
  integer :: n = 10, i, istat = 0
  real, pointer :: pp(:) => null()
! real, dimension(:), allocatable, target :: p
  real, allocatable, target :: p(:)

  allocate(p(n), stat = istat)
  if (istat /= 0) stop 'allocate error' 

  pp => p
  pp = [(real(i), i = 1, n, 1)]
  pp = pp / 2.

  p(1) = 2.

  print *, p

  nullify(pp)
  deallocate(p)
end program alloc

