%{
void yyerror(char* s);
#include <stdio.h>
#include <stdlib.h>
int getNoonTime(int time, char noon);
void isHourValid(int hour, int isNoon);
void isMinutsValid(int minuts);
%}

%union {int num; char id;}
%start time
%token <id> noon
%token <num> number
%type  <num>  time

%%

time : number ':' number noon '\n'      {isHourValid($1, 1); isMinutsValid($3); printf("%d:%d\n", getNoonTime($1, $4), $3);}
     | number ':' number '\n'           {isHourValid($1, 0); isMinutsValid($3); printf("%d:%d\n", $1, $3);}
     | number noon '\n'                 {isHourValid($1, 1); printf("%d:%d\n", getNoonTime($1, $2));}
     | number '\n'                      {isHourValid($1, 0); printf("%d:%d\n", $1);}
     | time number ':' number noon '\n'      {isHourValid($2, 1); isMinutsValid($4); printf("%d:%d\n", getNoonTime($2, $5), $4);}
     | time number ':' number '\n'           {isHourValid($2, 0); isMinutsValid($4); printf("%d:%d\n", $2, $4);}
     | time number noon '\n'                 {isHourValid($2, 1); printf("%d:%d\n", getNoonTime($2, $3));}
     | time number '\n'                      {isHourValid($2, 0); printf("%d:%d\n", $2);}
     ;

     
%%

int getNoonTime(int time, char noon)
{
    if (noon == 'a')
        return time;
    if (noon == 'p')
        return time + 12;
}

void isHourValid(int hour, int isNoon)
{
    if (isNoon && (hour < 0 || hour > 12))
    {
        printf("Error: With noon notation hour = [0-12]");
        exit(0);
    }
    else if (!isNoon && (hour < 0 || hour > 23))
    {
        printf("Error: Hour = [0-23]");
        exit(0);
    }
}

void isMinutsValid(int minuts)
{
    if (!(minuts <= 59 && minuts >= 0))
    {
        printf("Error: Minuts = [0-59]");
        exit(0);
    }
}

int main(void)
{
    return yyparse();
}

void yyerror(char* s) {fprintf(stderr, "%s\n", s);}