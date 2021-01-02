BINS=sdl_opengl_cube
LDLIBS=-lSDL2 -lm -lGL

all: $(BINS)

test: $(BINS)
	./sdl_opengl_cube

install: $(BINS)
	cp -a $(BINS) ~/bin

clean:
	rm -f sdl_opengl_cube $(OBJS)

