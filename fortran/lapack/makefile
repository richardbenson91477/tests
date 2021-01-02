BIN=lapack_1
FFLAGS=-O3 -march=$(IDM_CARCH)
LDLIBS=-llapack

%: %.f95
	gfortran $(FFLAGS) $^ -o $@ $(LDLIBS)

all: $(BIN)

test: all
	./$(BIN)

clean:
	rm -f $(BIN) *.o 

