GTKFLAGS=$(shell pkg-config gtk+-3.0 --cflags)
GTKLIBS=$(shell pkg-config gtk+-3.0 --libs)

CPPFLAGS += $(GTKFLAGS)
LDLIBS=$(GTKLIBS)
BINS=cgtk3 cgtk3b

all: $(BINS)

test: all
	./cgtk3

clean:
	rm -f $(BINS) *.o
