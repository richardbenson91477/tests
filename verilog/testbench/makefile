all: tb_iverilog

tb_iverilog: tb_iverilog.v
	iverilog -o $@ $^

test: all
	./tb_iverilog

clean:
	rm -f tb_iverilog


