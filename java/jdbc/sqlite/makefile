BN=jeo1_sqlite
include ../../makefile.base

LITEJAR=/prebuilt/jars/sqlite-jdbc.jar
CLASSPATH += $(LITEJAR):.

all: $(BN).class

test: all
	java -cp $(CLASSPATH) $(BN)

clean:
	rm -f *.class

