BN=jeo1
include ../../makefile.base

MDBJAR=/prebuilt/jars/mariadb-java-client.jar
CLASSPATH += $(MDBJAR):.

all: $(BN).class

test: all
	java -cp $(CLASSPATH) $(BN)

clean:
	rm -f *.class

