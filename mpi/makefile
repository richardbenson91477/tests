LDLIBS=-lm
CFLAGS+=-fopenmp -std=c11 -O1 -march=$(IDM_CARCH)
CC=mpicc

all: build

test: all
	mpirun -H katt:8,pepper:2 ./pi_2

build:
	./_build

clean:
	./_clean
