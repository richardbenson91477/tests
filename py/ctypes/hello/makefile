all: ext_hello.so

ext_hello.o: ext_hello.c
	$(CC) $(CFLAGS) -c $^

ext_hello.so: ext_hello.o
	$(CC) $(CFLAGS) -shared $^ -o $@

test: all
	./hello.py

clean:
	rm -f *.o *.so
