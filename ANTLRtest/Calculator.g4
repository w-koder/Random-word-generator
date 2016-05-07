grammar Calculator;

expr : expr '^' expr                       # Exp
     | '-' expr                            # Minus
     | expr operator = ('*' | '/') expr    # MulDiv
     | expr operator = ('+' | '-') expr    # AddSub
     | '(' expr ')'                        # Brackets
     | '|' expr '|'                        # Abs
     | INT                                 # Integer
     ;

//expr0: INT | '-' INT; //| '-' '(' expr ')' | '-' '|' expr '|';

MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
//EXP :   '^' ;
INT :   [0-9]+ ;
WS :    [ \t\r\n]+ -> skip;