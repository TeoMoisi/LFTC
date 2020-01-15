%{
#include <math.h>
#include "y.tab.h"
int lines = 0;
%}
%option noyywrap

SIGN		[+-]
DIGIT		[0-9]
NO		(0|[1-9]{DIGIT}*)
CST		[a-zA-Z]*|[1-9]*[0-9]*|0
ID		[a-zA-Z_][a-zA-Z_0-9]*{0,8}



%%

{NO}		{printf( "Number: %s\n", yytext );  return NO;}

"integer"		{printf( "Reserved word: %s\n", yytext );	return INT;}
"char"		{printf( "Reserved word: %s\n", yytext );	return CHAR;}
"boolean"		{printf( "Reserved word: %s\n", yytext );	return BOOL;}
"if"		{printf( "Reserved word: %s\n", yytext );	return IF;}
"else"		{printf( "Reserved word: %s\n", yytext );	return ELSE;}
"for"		{printf( "Reserved word: %s\n", yytext );	return FOR;}
"while"		{printf( "Reserved word: %s\n", yytext );	return WHILE;}
"begin"		{printf( "Reserved word: %s\n", yytext );	return BEG;}
"end"		{printf( "Reserved word: %s\n", yytext );	return END;}
"read"		{printf( "Reserved word: %s\n", yytext );	return RE;}
"write"		{printf( "Reserved word: %s\n", yytext );	return WR;}
"string"	{printf( "Reserved word: %s\n", yytext );	return STRING;}
"var"	{printf( "Reserved word: %s\n", yytext );	return VAR;}

{ID}		{printf( "Identifier: %s\n", yytext ); return ID;}
{CST}		{printf( "Constant: %s\n", yytext ); return CST;}

"+"		{printf( "Operator: %s\n", yytext );  return PLUS;}
"-"		{printf( "Operator: %s\n", yytext );  return MINUS;}
"*"		{printf( "Operator: %s\n", yytext );  return MULTIPLY;}
"/"		{printf( "Operator: %s\n", yytext );  return DIVIDE;}
"<"		{printf( "Operator: %s\n", yytext );  return LESS_THAN;}
">"		{printf( "Operator: %s\n", yytext );  return GREATER_THAN;}
"<="		{printf( "Operator: %s\n", yytext );  return LESS_THAN_OR_EQ;}
">="		{printf( "Operator: %s\n", yytext );  return GREATER_THAN_OR_EQ;}
"=="		{printf( "Operator: %s\n", yytext );  return DOUBLE_EQ;}
"&&"		{printf( "Operator: %s\n", yytext );  return AND;}
"||"		{printf( "Operator: %s\n", yytext );  return OR;}
"%"		{printf( "Operator: %s\n", yytext );  return MODULO;}
"!"		{printf( "Operator: %s\n", yytext );  return NOT;}
"!="		{printf( "Operator: %s\n", yytext );  return NOT_EQ;}
"="		{printf( "Operator: %s\n", yytext );  return EQ;}

"["		{printf( "Separator: %s\n", yytext );  return SQUARE_LEFT_B;}
"]"		{printf( "Separator: %s\n", yytext );  return SQUARE_RIGHT_B;}
"{"		{printf( "Separator: %s\n", yytext );  return CURLY_LEFT_B;}
"}"		{printf( "Separator: %s\n", yytext );  return CURLY_RIGHT_B;}
"("		{printf( "Separator: %s\n", yytext );  return ROUND_LEFT_B;}
")"		{printf( "Separator: %s\n", yytext );  return ROUND_RIGHT_B;}
":"		{printf( "Separator: %s\n", yytext );  return TWO_DOTS;}
";"		{printf( "Separator: %s\n", yytext );  return SEMI_COLON;}
","		{printf( "Separator: %s\n", yytext );  return COMA;}

[ \t\n]+ 	/* eat up whitespace */ {}
"{"[^}\n]*"}"	/* elimina comentarii */ {}
. 		{printf("Unknown symbol\n");	 return -1;}
