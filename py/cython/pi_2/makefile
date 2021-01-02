TARGET=pi_2
PYFLAGS=$(shell python3-config --cflags)
PYLIBS=$(shell python3-config --libs)

all: $(TARGET).so

$(TARGET).c: $(TARGET).pyx
	cython3 $^

$(TARGET).so: $(TARGET).c
	$(CC) $(CFLAGS) $(PYFLAGS) -shared $^ -o $@ $(PYLIBS)

test:
	python3 pi_driver.py

clean:
	rm -f $(TARGET).c $(TARGET).so
