CFLAGS=-Wall
CC=g++
SRC=cooke_analyzer.cpp cooke_definitions.cpp
OBJ=${SRC:.cpp=.o}

all: cooke_analyzer

cooke_analyzer: ${OBJ}
	${CC} ${CFLAGS} -o $@ ${OBJ}

clean:
	rm -f ${OBJ} cooke_analyzer
