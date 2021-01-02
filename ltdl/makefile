all: c.so main
LDFLAGS=-lltdl

c.o: c.c c.h
c.so: c.o
	$(CXX) $(CXXFLAGS) -shared -o $@ $^

main.o: main.c c.h
main: main.o
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)

test: all
	./main

clean:
	rm -f *.o *.so main


