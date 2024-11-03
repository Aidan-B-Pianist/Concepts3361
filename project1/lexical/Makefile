all: cooke_analyzer

cooke_analyzer: cooke_analyzer.o
	g++ -Wall cooke_analyzer

.c.o:
	g++ -Wall -c $<


test: cooke_analyzer cooke_analyzer.cpp
	./cooke_analyzer

clean:
	$(RM) cooke_analyzer.o