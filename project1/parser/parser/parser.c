#include <stdio.h>

#include "parser.h"
#include "front.h"

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
    printf("Enter <expr>\n");

    /* Parse the first term */
    term();

    /* As long as the next token is + or -, get
    the next token and parse the next term */
    while (nextToken == ADD_OP || nextToken == SUB_OP) {
        lex();
        term();
    }

    printf("Exit <expr>\n"); 
} /* End of function expr */

/* term
 * Parses strings in the language generated by the rule:
 * <term> -> <factor> {(* | /) <factor>)
 */
void term() 
{
    printf("Enter <term>\n");
    /* Parse the first factor */
    factor();
    /* As long as the next token is * or /, get the
    next token and parse the next factor */
    while (nextToken == MULT_OP || nextToken == DIV_OP) {
            lex();
            factor();
    }
    printf("Exit <term>\n");
} /* End of function term */

/* factor
 * Parses strings in the language generated by the rule:
 * <factor> -> id | int_constant | ( <expr )
 * */
void factor() 
{
    printf("Enter <factor>\n");
    /* Determine which RHS */
    if (nextToken == IDENT || nextToken == INT_LIT) {
        lex(); /* Get the next token */
    } else {
        /* If the RHS is (<expr>), call lex to pass over the 
        left parenthesis, call expr, and check for the right 
        parenthesis */
        if (nextToken == LEFT_PAREN) {
            lex(); 
            expr();

            if (nextToken == RIGHT_PAREN) {
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
    printf("Exit <factor>\n");;
} /* End of function factor */

static void error() 
{
    printf("Error (more is desired, but not implemented).\n");
}
