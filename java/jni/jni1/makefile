include ../../makefile.base

JFLAGS=-I$(JAVA_HOME)/include -I$(JAVA_HOME)/include/linux

all: jni1.class libfoo.so

libfoo.so: foo.c
	$(CC) $(CFLAGS) $(JFLAGS) -shared -o libfoo.so foo.c

test: all
	LD_LIBRARY_PATH=. java jni1

clean:
	rm -f *.class *.o *.so

