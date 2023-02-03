OBJECTS=
INCLUDES= -I./

all: ${OBJECTS}
	gcc main.c ${INCLUDES} ${OBJECTS} -g -O2 -o ./main.out

clean:
	rm ./main.out
	rm -rf *.dSYM/
	rm -rf ${OBJECTS}