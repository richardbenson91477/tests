FFLAGS=-O3 -march=$(IDM_CARCH)
LDLIBS=-lm
all: build

%: %.f
	gfortran $(FFLAGS) $^ -o $@

clean:
	./_clean
