OBJECTS=
INCLUDES= -I./
EXECUTIVE=fuckCpp

all: ${OBJECTS}
	gcc main.c ${INCLUDES} ${OBJECTS} -g -O2 -o ./${EXECUTIVE}

clean:
	rm ./${EXECUTIVE}
	rm -rf *.dSYM/
	rm -rf ${OBJECTS}