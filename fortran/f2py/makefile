all:
	f2py3 -c -m hello hello.f95

test: all
	./test_foo.py

clean:
	rm -f *.so
