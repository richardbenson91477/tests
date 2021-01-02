FFLAGS=-O3 -march=$(IDM_CARCH)
LDLIBS=-lm
all: build

%: %.f95
	gfortran $(FFLAGS) $^ -o $@

clean:
	./_clean
	rm -f *.mod
