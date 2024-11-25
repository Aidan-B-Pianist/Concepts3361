CFLAGS=-Wall
CC=g++
SRC=cooke_parser.cpp cooke_parser_definitions.cpp
OBJ=${SRC:.cpp=.o}

all: cooke_parser

cooke_parser: ${OBJ}
	${CC} ${CFLAGS} -o $@ ${OBJ}

clean:
	rm -f ${OBJ} cooke_parser

