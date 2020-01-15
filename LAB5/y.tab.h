/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     NO = 258,
     ID = 259,
     CST = 260,
     INT = 261,
     CHAR = 262,
     BOOL = 263,
     IF = 264,
     ELSE = 265,
     FOR = 266,
     WHILE = 267,
     BEG = 268,
     END = 269,
     RE = 270,
     WR = 271,
     STRING = 272,
     SQUARE_LEFT_B = 273,
     SQUARE_RIGHT_B = 274,
     CURLY_LEFT_B = 275,
     CURLY_RIGHT_B = 276,
     ROUND_LEFT_B = 277,
     ROUND_RIGHT_B = 278,
     TWO_DOTS = 279,
     SEMI_COLON = 280,
     SPACE = 281,
     COMA = 282,
     DOT = 283,
     MINUS = 284,
     PLUS = 285,
     DIVIDE = 286,
     MULTIPLY = 287,
     OR = 288,
     AND = 289,
     LESS_THAN = 290,
     GREATER_THAN = 291,
     LESS_THAN_OR_EQ = 292,
     EQ = 293,
     GREATER_THAN_OR_EQ = 294,
     DOUBLE_EQ = 295,
     MODULO = 296,
     NOT = 297,
     NOT_EQ = 298,
     VAR = 299
   };
#endif
/* Tokens.  */
#define NO 258
#define ID 259
#define CST 260
#define INT 261
#define CHAR 262
#define BOOL 263
#define IF 264
#define ELSE 265
#define FOR 266
#define WHILE 267
#define BEG 268
#define END 269
#define RE 270
#define WR 271
#define STRING 272
#define SQUARE_LEFT_B 273
#define SQUARE_RIGHT_B 274
#define CURLY_LEFT_B 275
#define CURLY_RIGHT_B 276
#define ROUND_LEFT_B 277
#define ROUND_RIGHT_B 278
#define TWO_DOTS 279
#define SEMI_COLON 280
#define SPACE 281
#define COMA 282
#define DOT 283
#define MINUS 284
#define PLUS 285
#define DIVIDE 286
#define MULTIPLY 287
#define OR 288
#define AND 289
#define LESS_THAN 290
#define GREATER_THAN 291
#define LESS_THAN_OR_EQ 292
#define EQ 293
#define GREATER_THAN_OR_EQ 294
#define DOUBLE_EQ 295
#define MODULO 296
#define NOT 297
#define NOT_EQ 298
#define VAR 299




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

