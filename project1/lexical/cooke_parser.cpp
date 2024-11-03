#include <iostream>
#include <fstream>
#include <ctype.h>

#include "cooke_definitions.cpp"
#include "cooke_parser_definitions.cpp"



using namespace std;

int nextToken;

static int charClass;
static char lexeme [100];
static char nextChar;
static int lexLen;
static FILE *in_fp;
string tokenString;
int lineNumber = 1;

static void addChar();
static void getChar();
static void getNonBlank();
int lex();


static void error();

/**
 * This is the example Recursive-Descent Parser in pp. 181 - 185 in the 
 * textbook 
 *
 * Sebesta, R. W. (2012). Concepts of Programming Languages. 
 * Pearson, 10th edition.
 *
 *
 * */

/* expr
 * Parses strings in the language generated by the rule:
 * <expr> -> <term> {(+ | -) <term>}
 */

void expr() 
{
    //cout << "Enter <expr>" << endl;

    /* Parse the first term */
    term();

    /* As long as the next token is + or -, get
    the next token and parse the next term */
    while (nextToken == ADD_OP || nextToken == SUB_OP) {
        lex();
        term();
    }

    //cout << "Exit <expr>" << endl; 
} /* End of function expr */

/* term
 * Parses strings in the language generated by the rule:
 * <term> -> <factor> {(* | /) <factor>)
 */
void term() 
{
    //cout << "Enter <term>" << endl;
    /* Parse the first factor */
    factor();
    /* As long as the next token is * or /, get the
    next token and parse the next factor */
    while (nextToken == MULT_OP || nextToken == DIV_OP) {
            lex();
            factor();
    }
    //cout << "Exit <term>" << endl;
} /* End of function term */

/* factor
 * Parses strings in the language generated by the rule:
 * <factor> -> id | int_constant | ( <expr )
 * */
void factor() 
{
    //cout << "Enter <factor>" << endl;
    /* Determine which RHS */
    if (nextToken == IDENT || nextToken == INT_LIT) {
        lex(); /* Get the next token */
    } else {
        /* If the RHS is (<expr>), call lex to pass over the 
        left parenthesis, call expr, and check for the right 
        parenthesis */
        if (nextToken == OPEN_PAREN) {
            lex(); 
            expr();

            if (nextToken == CLOSE_PAREN) {
                lex(); 
            } else { 
                error();
            }
        } /* End of if (nextToken == ... */
        /* It was not an id, an integer literal, or a left parenthesis */
        else 
        { 
            error(); 
        }
    } /* End of else */
    //cout << "Exit <factor>" << endl;
} /* End of function factor */

static void error() 
{
    cout << "Error on line " << lineNumber << ": The next lexeme was " << lexeme << " and the next token was " << tokenString << endl;
}

static void getChar() {
    if ((nextChar = getc(in_fp)) != EOF) {
        if (isalpha(nextChar))
            charClass = LETTER;
        else if (isdigit(nextChar))
            charClass = DIGIT;
        else charClass = UNKNOWN;
    } else {
        charClass = EOF;
    }
}

static void getNonBlank() {
    while (isspace(nextChar)) {
        if('\n' == nextChar) {
            lineNumber++;
        }
        getChar();
    } 
}

static void addChar() {
    if (lexLen <= 98) {
        lexeme[lexLen++] = nextChar;
        lexeme[lexLen] = 0;
    } else {
        printf("Error - lexeme is too long \n");
    }
}

/* Get the string value of each token*/
string valueOf(int token) {
    switch (token)
    {
    case 0:
        return "LETTER";
        break;
        
    case 1:
        return "DIGIT";
        break;
    
    case 99:
        return "UNKNOWN";
        break;

    case 10:
        return "ASSIGN_OP";
        break;

    case 11:
        return "LESSER_OP";
        break;

    case 12:
        return "GREATER_OP";
        break;
    
    case 13:
        return "EQUAL_OP";
        break;

    case 14:
        return "NEQUAL_OP";
        break;

    case 15:
        return "LEQUAL_OP";
        break;
    
    case 16:
        return "GEQUAL_OP";
        break;

    case 17:
        return "OPEN_PAREN";
        break;
    
    case 18:
        return "CLOSE_PAREN";
        break;

    case 19:
        return "ADD_OP";
        break;

    case 20:
        return "SUB_OP";
        break;

    case 21:
        return "MULT_OP";
        break;

    case 22:
        return "DIV_OP";
        break;

    case 23:
        return "MOD_OP";
        break;

    case 24:
        return "BOOL_AND";
        break;

    case 25:
        return "BOOL_OR";
        break;

    case 26:
        return "BOOL_NOT";
        break;

    case 27:
        return "SEMICOLON";
        break;

    case 28:
        return "KEY_IN";
        break;

    case 29:
        return "KEY_OUT";
        break;

    case 30:
        return "KEY_IF";
        break;

    case 31:
        return "KEY_ELSE";
        break;

    case 32:
        return "OPEN_CURL";
        break;

    case 33:
        return "CLOSE_CURL";
        break;

    case 34:
        return "INT_LIT";
        break;

    case 35:
        return "IDENT";
        break;

    default:
        return "";
        break;
    }
}

/* look up operators and parantheses*/
static int lookup(char ch) {
    switch (ch) {
        case '=':
            addChar();
            getChar();
            if(nextChar == '=') {
                addChar();
                nextToken = EQUAL_OP;
            }
            else {
                nextToken = ASSIGN_OP;
            }
            break;
        case '!':
            addChar();
            getChar();
            if(nextChar == '=') {
                addChar();
                nextToken = NEQUAL_OP;
            }
            else {
                nextToken = BOOL_NOT;
                return nextToken;
            }
            break;
        case '<':
            addChar();
            getChar();
            if(nextChar == '=') {
                addChar();
                nextToken = LEQUAL_OP;
            }
            else {
                nextToken = LESSER_OP;
                return nextToken;
            }
            break;
        case '>':
            addChar();
            getChar();
            if(nextChar == '=') {
                addChar();
                nextToken = GEQUAL_OP;
            }
            else {
                nextToken = GREATER_OP;
                return nextToken;
            }
            break;
        case '(':
            addChar();
            nextToken = OPEN_PAREN;
            break;
        case ')':
            addChar();
            nextToken = CLOSE_PAREN;
            break;
        case '+':
            addChar();
            nextToken = ADD_OP;
            break;
        case '-':
            addChar();
            nextToken = SUB_OP;
            break;
        case '*':
            addChar();
            nextToken = MULT_OP;
            break;
        case '/':
            addChar();
            nextToken = DIV_OP;
            break;
        case ';':
            addChar();
            nextToken = SEMICOLON;
            break;
        case '{':
            addChar();
            nextToken = OPEN_CURL;
            break;
        case '}':
            addChar();
            nextToken = CLOSE_CURL;
            break;
        case '&':
            addChar();
            getChar();
            if(nextChar == '&') {
                addChar();
                nextToken = BOOL_AND;
            }
            else {
                nextToken = EOF;
            }
            break;
        case '|':
            addChar();
            getChar();
            if(nextChar == '|') {
                addChar();
                nextToken = BOOL_OR;
            }
            else {
                nextToken = EOF;
            }
            break;
        default:
            addChar();
            nextToken = UNKNOWN;
            break;
    }
    getChar();
    return nextToken;
}

int lex() {
    lexLen = 0;
    getNonBlank();

    string str = "";
    switch (charClass) {
        /* Parse identifiers */
        case LETTER:
            addChar();
            getChar();
            while (charClass == LETTER || charClass == DIGIT) {
                addChar();
                getChar();
            }
            str = lexeme;
            if(!str.compare("input")) {
                    nextToken = KEY_IN;
                }
            else if(!str.compare("output")) {
                nextToken = KEY_OUT;
            }
            else if(!str.compare("if")) {
                nextToken = KEY_IF;
            }
            else if(!str.compare("else")) {
                nextToken = KEY_ELSE;
            }
            else {
                nextToken = IDENT;
            }
            str = "";
            break;

        /* Parse integer literals */
        case DIGIT:
            addChar();
            getChar();
            while (charClass == DIGIT) {
                addChar();
                getChar();
            }
            nextToken = INT_LIT;
            break;

        /* Parentheses and operators */
        case UNKNOWN:
            lookup(nextChar);
            break;

        /* EOF */
        case EOF:
            nextToken = EOF;
            lexeme[0] = 'E';
            lexeme[1] = 'O';
            lexeme[2] = 'F';
            lexeme[3] = 0;
            break;
    } /* End of switch */

    tokenString = valueOf(nextToken);
    

    return nextToken;
} /* End of function lex */

int main(int argc, char* argv[]) {

    // in_fp = fopen(argv[1], "r");
    in_fp = fopen("test.dc", "r");

    for(int i = 0; i < argc; i++) {
        cout << argv[i];
    }
    cout << endl;

    if (in_fp == NULL) {
        cout << "ERROR - cannot open file \n" << endl;
    }
    else {
        cout << "Cooke Parser :: R11837228\n" << endl;
        getChar();
        do {
            lex();
            expr();
        } while (nextToken != EOF);
    }
    return 0;
}