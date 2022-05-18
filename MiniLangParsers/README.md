# Mini lang parser

The task was to create interpreters of languages more friendly to people who perform certain operations.

## Turtle parser

For given instruction make turtle program moving certain direction and print the specified errors.

List of instruction:

* P [number] -- select color pen num [1-15] (default 1)
* D -- pen down
* U -- pen up
* W [number] -- move to west by number
* N [number] -- move north by number
* E [number] -- move east by number
* S [number] -- move south by number

## Yacc time parser

The input is different time formats and the output prints you the hour: minute format.

Available formats:

* hour : minute [pm|am]
* hour : minute
* hour [pm|am]
* hour

To build (window):

```cmd
win_bison -d timeParser.y; win_flex timeParser.l; gcc lex.yy.c timeParser.tab.c -o timeParser.exe
```

## Yacc lex calculator

A simple calculator that supports 5 instructions on integers:

* Assigning to single-letter variables
* Addition
* Subtraction
* Printing
* Exit instruction

Code is made with: [https://www.youtube.com/watch?v=__-wUHG2rfM](https://www.youtube.com/watch?v=__-wUHG2rfM)
