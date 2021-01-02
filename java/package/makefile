include ../makefile.base
JAR=j.jar
OBJS=j1/test1.class j2/test2.class

all: $(JAR)

$(JAR): $(OBJS)
	jar cfmv $(JAR) META-INF/MANIFEST.MF .

test: all
	java -jar $(JAR)

clean:
	rm -f $(JAR) $(OBJS)

