BIN=main
OBJS=iswap.o main.o

$(BIN): $(OBJS)
	gfortran -o $@ $^

all: $(OBJS)

test: all
	./$(BIN)

clean:
	rm -f $(BIN) $(OBJS)

