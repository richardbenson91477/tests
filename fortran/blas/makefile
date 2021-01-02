BIN=blas_1
FFLAGS=-O3 -march=$(IDM_CARCH)
LDLIBS=-lblas -lm

%: %.f95
	gfortran $(FFLAGS) $^ -o $@ $(LDLIBS)

all: $(BIN)

test: all
	./$(BIN)

clean:
	rm -f $(BIN) *.c *.o 

