%{
#include "timeParser.tab.h"
%}

%%
"pm"|"am"           {yylval.id = yytext[0]; return noon;}
[0-9]?[0-9]          {yylval.num = atoi(yytext); return number;}
[ \t\r]       ;
[:\n]             {return yytext[0];}
.               {ECHO; yyerror(" unexpected character");}
%%

int yywrap(void)
{
    return 1;
}