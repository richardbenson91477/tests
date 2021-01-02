
OBJS=csdl2.o
LIBS=$(OBJS)
LDLIBS=-lSDL2 -lSDL2_mixer -lSDL2_image

all: csdl2

csdl2: $(LIBS)

test: all
	./csdl2

clean:
	rm -f csdl2 $(OBJS)

