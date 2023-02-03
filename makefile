OBJECTS=
INCLUDES= -I./

all: ${OBJECTS}
	gcc main.c ${INCLUDES} ${OBJECTS} -g -O2 -o ./main

clean:
	rm ./main
	rm -rf ${OBJECTS}