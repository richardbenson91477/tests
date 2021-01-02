
OBJS=so.o so_imp.o
INCS=so.h
SOLIB=so.so

all: so_imp

$(OBJS): $(INCS)

$(SOLIB): so.o
	$(CC) $(CFLAGS) -shared -o $@ $^

so_imp: so_imp.o $(SOLIB)
	$(CC) $(CFLAGS) -o $@ $^

test: all
	LD_LIBRARY_PATH=. ./so_imp

clean:
	rm -f so_imp $(SOLIB) $(OBJS)

