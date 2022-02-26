program -> (declare | func)* EOF

declare -> (INT | FLOAT) ID (CM ID)* SM

func -> (INT | FLOAT) ID LP paraList? RP scope
scope -> LB stmt* RB
stmt -> declare | assignmentStmt | callStmt | returnStmt

assignmentStmt -> ID EQ expr SM

callStmt -> ID LP paraList? RP SM
paraList -> para (CM para)*

returnStmt -> RETURN expr SM

expr -> exprSub ADD expr
      | callStmt
exprSub -> term SUB term
term -> term (MUL | DIV) lit
lit -> LB lit RB
     | INTLIT
     | FLOATLIT
     | ID

INT -> 'Int'
FLOAT -> 'Float'
RETURN -> 'Return'

LP -> '('
RP -> ')'
LB -> '{'
RB -> '}'
SM -> ';'
CM -> ','
EQ -> '='
ADD -> '+'
SUB -> '-'
MUL -> '*'
DIV -> '/'

ID -> [A-Za-z_][A-Za-z0-9_]*

INTLIT -> [0-9]+

FLOATLIT -> INT_PART DEC_PART? EXP_PART?
INT_PART -> [0-9]+
DEC_PART -> '.'[0-9]+
EXP_PART -> [eE][+-]?[0-9]+

WS -> [ \t\r\n] -> skip