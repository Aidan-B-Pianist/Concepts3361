OBJ=main.o calculator.o 
CC=gcc
TARGET=assignment_1

all: assignment_1

${OBJ}: calculator.h

assignment_1: $(OBJ)
	${CC} ${CFLAGS} -o $@ ${OBJ}

clean:
	rm -f $(TARGET) $(OBJ)

