c c/o https://en.wikibooks.org/wiki/Fortran/Fortran_examples
c Area of a triangle - Heron's formula
      implicit none
      integer a, b, c
      real s, area

   10 read (*,*) a, b, c
      s = (a + b + c) / 2.0
      area = sqrt(s * (s - a) * (s - b) * (s - c))

      write (*,*) a, b, c, area
      go to 10

      END

